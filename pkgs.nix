let
  pinned_pkgs = import
    (builtins.fetchTarball {
      # https://nixos.wiki/wiki/FAQ/Pinning_Nixpkgs
      name = "nixpkgs-pinned";
      url = "https://github.com/NixOS/nixpkgs/archive/ca77296380960cd497a765102eeb1356eb80fed0.tar.gz";
      # url = "https://github.com/NixOS/nixpkgs/archive/9d7410bfe2ab00cab2780e13fad7cc828705eaec.tar.gz";
      # sha256 = "ce8603ff66766c797896b2e8e03370cd482d2b12e460cfb039d06dabad459cdb";
      # sha256 = "254rnp87ygkfr5jfxz2lamhzqm5blrz55flpy3p6l654vafd72pf";
      sha256 = "sha256:1airrw6l87iyny1a3mb29l28na4s4llifprlgpll2na461jd40iy";
    })
  ;
in
pinned_pkgs
