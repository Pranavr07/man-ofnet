from .io import IO


_MAIN_BANNER = r"""{}
      █▀▄▀█ ▄▀█ █▄░█  █▀█ █▀▀  █▄░█ █▀▀ ▀█▀
      █░▀░█ █▀█ █░▀█  █▄█ █▀░  █░▀█ ██▄ ░█░
  

""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.Style.BRIGHT)


def get_main_banner(version):
    return _MAIN_BANNER.replace('[_V_]', version)