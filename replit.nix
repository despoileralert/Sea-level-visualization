{ pkgs }: {
  deps = [
    pkgs.python38Full
    pkgs.python38Packages.matplotlib
    pkgs.python38Packages.pandas
    pkgs.python38Packages.scipy
    pkgs.python38Packages.numpy
    pkgs.python38Packages.seaborn
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}