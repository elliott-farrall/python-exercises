{ mkShell
, pkgs
, lib
, inputs
, system
, ...
}:

mkShell rec {
  name = "poetry";

  buildInputs = inputs.self.checks.${system}.pre-commit.enabledPackages;
  packages = with pkgs; [
    python310
    poetry
    ruff
    zlib
  ];

  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib:${lib.makeLibraryPath packages}:";

  POETRY_VIRTUALENVS_IN_PROJECT = true;
  shellHook = ''
    poetry env use $(which python)
    poetry install
  '' + inputs.self.checks.${system}.pre-commit.shellHook;
}
