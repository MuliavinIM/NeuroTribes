{
  description = "NeuroTribes development environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      projectPython = pkgs.python3.withPackages (ps: [
        ps.pip
        ps.setuptools
        ps.pytest
        ps.pygame 
      ]);
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          projectPython
          pkgs.git
        ];

        shellHook = ''
          export PYTHONPATH="$PWD/src"
        '';
      };
    };
}
