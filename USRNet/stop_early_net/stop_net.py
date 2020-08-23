import time
import os
import numpy as np
import torch
from torch import nn


class StopNet:
    def __init__(self, config):
        self.channels_in = config['channels_in']
        self.loss = self.define_loss()
        self.base_dir = r'./'

    def build_network(self):  # BASE version. Other modes override this function
        """

        :return:
        """

        class Flatten(nn.Module):
            def forward(self, x):
                return x.view(x.size()[0], -1)

        net = nn.Sequential(
            nn.Conv2d(in_channels=self.channels_in, out_channels=32, kernel_size=3, padding=1, stride=2),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1, stride=2, padding_mode='replicate'),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1, stride=2, padding_mode='replicate'),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1, stride=2, padding_mode='replicate'),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1, stride=2, padding_mode='replicate'),
            nn.ReLU(),
            Flatten(),
            nn.Linear('enter the proper size', 1)
        ).to(self.device)
        return net

    def define_loss(self):
        return torch.nn.BCELoss()

    def define_opt(self):
        return torch.optim.Adam(self.net.parameters(), lr=1e-4)

    def forward(self, input_tensor):  # BASE version. Other modes override this function
        return self.net(input_tensor)

    def train(self, data_loader_object, cumulative_scale):
        # epochs
        for e in range(self.epochs):
            t = time.time()
            np.random.seed()
            self.optimizer.zero_grad()

            if e % save_every == save_every - 1:
                print(f'saved model at epoch {e}')
                self.save_model(epoch=e, overwrite=False, cumulative_scale=cumulative_scale)

            # iterations per epochs
            it = 0
            for (image, index, gt_label) in data_loader_object:
                # concat image and index
                pred_label = self.forward(input_tensor.to(self.device))
                loss = self.loss(pred_label, gt_label)
                it += 1
            print(f'epoch:{e}, loss:{loss.item():.7f}. Time: {(time.time() - t):.2f}, lr={self.optimizer.param_groups[0]["lr"]}')
            loss.backward()

            self.optimizer.step()
            self.writer.add_scalars('loss', {'loss': loss.item()})
            self.writer.add_scalars('lr', {'lr': self.optimizer.param_groups[0]["lr"]})

        # save final trained model as well
        self.save_model(epoch=e, overwrite=False, cumulative_scale=cumulative_scale)
        self.writer.close()
        return

    def save_model(self, epoch=None, scale=None, overwrite=False, cumulative_scale=2):
        """
        Saves the model (state-dict, optimizer and lr_sched
        :return:
        """
        if overwrite:
            checkpoint_list = [i for i in os.listdir(os.path.join(self.base_dir)) if i.endswith('.pth.tar')]
            if len(checkpoint_list) != 0:
                os.remove(os.path.join(self.base_dir, checkpoint_list[-1]))

        filename = 'checkpoint{}{}.pth.tar'.format('' if epoch is None else '-e{:05d}'.format(epoch),
                                                   '' if scale is None else '-s{:02d}'.format(scale))
        folder = os.path.join(self.base_dir, 'saved_models', f'cumulative_scale_{cumulative_scale}')
        os.makedirs(folder, exist_ok=True)
        torch.save({'sd': self.net.state_dict(),
                    'opt': self.optimizer.state_dict()},
                   # 'lr_sched': self.scheduler.state_dict()},
                   os.path.join(folder, filename))

    def load_model(self, filename):
        # TODO: Not called anywhere, no ability to load saved model
        checkpoint = torch.load(filename)
        self.net.load_state_dict(checkpoint['sd'])
        self.optimizer.load_state_dict(checkpoint['opt'])
        # self.scheduler.load_state_dict(checkpoint['lr_sched'])
