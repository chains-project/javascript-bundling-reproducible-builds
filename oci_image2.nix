{ pkgs ? import ./pkgs.nix { }
, # pkgsLinux ? import ./pkgs.nix {}
}:
# https://ryantm.github.io/nixpkgs/builders/images/dockertools/
let
  node_image = pkgs.dockerTools.pullImage {
    imageName = "node";
    # 24.4.1-alpine
    imageDigest = "sha256:820e86612c21d0636580206d802a726f2595366e1b867e564cbc652024151e8a";
    sha256 = "sha256-UYQ174DFDTui8hmnKUQ+AF3VOEvWhv9Zvc+a7XlFILA=";

  };
in
let
  # https://nix.dev/tutorials/nixos/building-and-running-docker-images.html
  image = pkgs.dockerTools.buildImage {
    name = "rb-24.4.1-alpine";
    tag = "latest";
    # fromImage = "docker.io/library/archlinux";
    fromImage = node_image;

    # https://ryantm.github.io/nixpkgs/builders/images/dockertools/
    #copyToRoot = pkgs.buildEnv {
    #  name = "x2";
    #paths = with pkgs; [ bash nodejs coreutils  ];
    #pathsToLink = [ "/bin" ];
    #};
    # config = {
    #   Cmd =["ls" "/"];
    # };
    # includeNixDB=true;
  };
in
image
#node_image
