from abc import ABCMeta


class DeviceTreeMixin(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._make_targets_opts["dtbs"] = self._get_base_make_vars()

    def make_dtbs(self):
            self.make_caller("dtbs", cwd=self.kernel_src_path)
