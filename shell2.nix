{ pkgs ? import (builtins.fetchTarball {
    # https://nixos.wiki/wiki/FAQ/Pinning_Nixpkgs
    name = "nixpkgs-pinned";
    url = "https://github.com/NixOS/nixpkgs/archive/88983d4b665fb491861005137ce2b11a9f89f203.tar.gz";
    # sha256 = "ce8603ff66766c797896b2e8e03370cd482d2b12e460cfb039d06dabad459cdb";
    sha256 = "154rnp87ygkfr5jfxz2lamhzqm5blrz55flpy3p6l654vafd72pf";

  }) {}
}: pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    (python3.withPackages (pyPkgs: [ pyPkgs.requests pyPkgs.pandas ]))
    nodejs_23

  ];
}
