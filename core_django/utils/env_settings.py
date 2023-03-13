from environ import Env


class EnvironSetting:
    def __init__(self):
        self.env = Env()

    def get_env(self, base_dir):
        env_path = base_dir / ".env"
        if env_path.exists():
            with env_path.open("rt", encoding="utf8") as e:
                self.env.read_env(e, overrides=True)
        return self.env
