{ pkgs ? import ./pkgs.nix { }
, # pkgsLinux ? import ./pkgs.nix {}
}:
# https://nix.dev/tutorials/nixos/building-and-running-docker-images.html
pkgs.dockerTools.buildImage {
  name = "image2";
  tag = "latest";
  # fromImage = "docker.io/library/archlinux";

  # https://ryantm.github.io/nixpkgs/builders/images/dockertools/
  copyToRoot = pkgs.buildEnv {
    name = "x";
    paths = with pkgs; [ bash coreutils nodejs_20 ];
    pathsToLink = [ "/bin" ];
  };
  # config = {
  #   Cmd =["ls" "/"];
  # };
  # includeNixDB=true;
}
