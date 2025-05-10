---
title: Linux 使用笔记（进阶）
date: 2025/05/10
categories: 软件使用
tags: [SELinux, RockyLinux]
---

## 引言

从 2018 年开始入门 Linux，已经 7 年了。
从 Deepin 到 Manjaro，再到 Rocky Linux。
中间也尝试过 ArchLinux, Debian, Ubuntu, CentOS等等。

一开始入门是能用就行，折腾桌面环境。
到现在开始考虑一些安全性，长期的稳定性，不再为了图省事直接关闭防火墙和 SELinux。
每一行代码都想要理解含义。
理解配置的逻辑和哲学。

## `Rocky Linux`

用 `Rocky Linux` 用的还不多，在此写一些备忘。

`Rocky Linux` 是 CentOS 替代品，适用于服务器。

- 默认使用 `SELinux`，

- 使用`Cockpit` 面版，

- 使用 LVM 和 `xfs`文件系统。
`xfs`文件系统，性能高，适合处理大文件，并行写入，可以不停机扩容，但是不支持缩容，跨平台兼容性差。

## LVM（逻辑卷管理）

| 层级         | 作用         | 类比       |
| ---------- | ---------- | -------- |
| **物理卷 PV** | 实际的硬盘或分区   | 地基       |
| **卷组 VG**  | 若干物理卷组合的池子 | 水泥池      |
| **逻辑卷 LV** | 从卷组中划分出来的卷 | 建在池子里的房间 |

可以用 `pvdispaly` 查看，或者简写为 `pvs`。同理 `vgs` 和 `lvs`


### 示例

先用 `lsblk` 查看硬盘情况。只有 `nvme0n1p3` 分区中有 3 个 lv：
```shell
AMD-ZQW-srv ➜  ~ lsblk -f
NAME        FSTYPE      FSVER    LABEL UUID                                   FSAVAIL FSUSE% MOUNTPOINTS
sda
└─sda1      ntfs                 Music 123419620B147062                         37.4G    98% /hdd7
nvme0n1
├─nvme0n1p1 vfat        FAT32          1234-B31A                               562.6M     6% /boot/efi
├─nvme0n1p2 xfs                        1234d41c-4f32-4759-9d14-652ee9c5688f     64.6M    93% /boot
└─nvme0n1p3 LVM2_member LVM2 001       1234Wo-pyLw-p278-rTFa-D4ix-7ob1-jEKxpp
  ├─rl-root xfs                        12347aef-b5a5-4034-8b01-1449de8cc13f     21.7G    69% /
  ├─rl-swap swap        1              1234c97d-5ec9-4720-84f2-30440f4269d3                  [SWAP]
  └─rl-home xfs                        1234270f-41f8-4d69-bd4d-43e20c790d82    768.9G     9% /home

```
3个 lv 中，有一个是 swap，另外两个 lv 的文件格式都是 xfs。


再 `df` 一下，作为参考：
```shell
AMD-ZQW-srv ➜  ~ df -hT
Filesystem          Type      Size  Used Avail Use% Mounted on
devtmpfs            devtmpfs  4.0M     0  4.0M   0% /dev
tmpfs               tmpfs      16G   84K   16G   1% /dev/shm
tmpfs               tmpfs     6.1G   11M  6.1G   1% /run
efivarfs            efivarfs  128K   36K   88K  30% /sys/firmware/efi/efivars
/dev/mapper/rl-root xfs        70G   49G   22G  69% /
/dev/mapper/rl-home xfs       845G   76G  769G   9% /home
/dev/nvme0n1p2      xfs       960M  896M   65M  94% /boot
/dev/nvme0n1p1      vfat      599M   37M  563M   7% /boot/efi
/dev/sda1           fuseblk   1.9T  1.8T   38G  98% /hdd7
tmpfs               tmpfs     3.1G  200K  3.1G   1% /run/user/1000
```

`nvme0n1p3` 分区是一个 pv：
```shell
AMD-ZQW-srv ➜  ~ sudo pvs
  PV             VG Fmt  Attr PSize   PFree
  /dev/nvme0n1p3 rl lvm2 a--  929.92g    0
```

`/dev/nvme0n1p3` pv 中的三个 lv 组成一个名为 `rl` (Rocky Linux) 的 vg：
```shell
AMD-ZQW-srv ➜  ~ sudo vgs
  VG #PV #LV #SN Attr   VSize   VFree
  rl   1   3   0 wz--n- 929.92g    0
```
查看所有的 lv，3 个 lv 分别为 `home` `root` `swap` ，全都属于 vg `rl`：
```shell
AMD-ZQW-srv ➜  ~ sudo lvs
  LV   VG Attr       LSize    Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  home rl -wi-ao---- <844.63g
  root rl -wi-ao----   70.00g
  swap rl -wi-ao----   15.29g
```

## DNF 和 rpm

`Rocky Linux` 使用 `dnf` 和 `rpm` 管理软件包。

| 功能       | 命令                                        |
| -------- | ----------------------------------------- |
| 查找软件包    | `dnf search <关键词>`                        |
| 安装软件包    | `dnf install <软件包名>`                      |
| 删除软件包    | `dnf remove <软件包名>`                       |
| 更新所有包    | `dnf upgrade`              |
| 查看包信息    | `dnf info <软件包名>`                         |
| 清理缓存     | `dnf clean all`                           |
| 显示所有可更新包 | `dnf check-update`                        |
| 启用/禁用源   | `dnf config-manager --set-enabled <repo>` |
| 查看软件源    | `dnf repolist`                            |

| 工具    | 作用                        |
| ----- | ------------------------- |
| `rpm` | 管理单个 `.rpm` 包（安装、查询、卸载等）  |
| `dnf` | **依赖于 `rpm`**，自动处理依赖，连接仓库 |


## zsh



### 硬盘挂载

## journalctl 查看日志

## Podman(Docker)

开放端口

```shell
sudo semanage port -a -t http_port_t -r 's0' -p tcp xxxx
```

允许访问目录，以及递归的子目录

```shell
sudo semanage fcontext -a -f a -t container_file_t -r 's0' '/home/zqw/(/.*)?'
```



## SELinux

查看 SELinux 状态：
`getenforce`

关闭：
`setenforce 0`

开启：
`setenforce 1`

## Firewall


## Systemctl

## 初始化与用户、权限管理

出于安全考虑修改 `ssh` 的默认端口。

## 引导

## 致谢

所有为 ChatGPT 提供训练素材的人。