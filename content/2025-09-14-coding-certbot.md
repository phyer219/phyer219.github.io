---
title: 用 certbot 手动获取受信任的 SSL证，并实现对 NextCloud 容器 80 端口的 SSL 访问
date: 2025-09-14
category: coding
tags:
  - SSL
  - certbot
slug: certbot
---

## SSL加密

在使用自己搭建的服务，如 `emby` ,`nextcloud`, `immich` 时，如果使用域名访问，当没有进行受信任的 SSL 加密时，对应的手机 app 会连不上，提醒，或报错。

最简单的方式是用 `certbot` 获取一个 90 天期限的 SSL 证书，到期后再更新。此篇博客做一备忘。

## 证书获取过程

安装好certbot后，执行以下命令手动获取 SSL 证书，并用在域名上添加一条 txt 解析的方式进行域名验证：

```bash
certbot certonly --manual --preferred-challenges dns -d xxx.xxx.com
```

按提示在域名提供商处添加记录：

```bash
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Requesting a certificate for xxx.xxx.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name:

_acme-challenge.xxx.xxx.com.

with the following value:

GxxxxxxxxxxxxxQ

Before continuing, verify the TXT record has been deployed. Depending on the DNS
provider, this may take some time, from a few seconds to multiple minutes. You can
check if it has finished deploying with aid of online tools, such as the Google
Admin Toolbox: https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.xxx.xxx.com.
Look for one or more bolded line(s) below the line ';ANSWER'. It should show the
value(s) you've just added.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/xxx.xxx.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/xxx.xxx.com/privkey.pem
This certificate expires on 2025-12-13.
These files will be updated when the certificate renews.

NEXT STEPS:
- This certificate will not be renewed automatically. Autorenewal of --manual certificates requires the use of an authentication hook script (--manual-auth-hook) but one was not provided. To renew this certificate, repeat this same certbot command before the certificate's expiry date.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

`.pem`、`.crt`、`.key` 本质上都是文本格式的证书/密钥文件，只是扩展名不同而已。可以直接需要复制或改名：

```bash
fullchain.pem ->.crt
privkey.pem ->.key
```

正确设置权限，参考如下：

```bash
-rw-r--r--. 1 zqw zqw 2.8K Sep 14 17:40 server.crt
-rw-------. 1 zqw zqw  227 Sep 14 17:40 server.key
```

## 代理的 Podman 文件，代理容器的配置文件示例

`nextcloud-proxy.container`:

```bash
[Container]
ContainerName=nextcloud-proxy
Pod=nextcloud.pod
Image=docker.io/library/httpd:2.4
Volume=/xxx/extra-proxy.conf:/usr/local/apache2/conf/extra/proxy.conf:ro,Z
Volume=/xxx/httpd.conf:/usr/local/apache2/conf/httpd.conf:ro,Z
Volume=/xxx/server.crt:/usr/local/apache2/conf/server.crt:ro,Z
Volume=/xxx/server.key:/usr/local/apache2/conf/server.key:ro,Z
```

`httpd.conf`

```bash
# Real-time info on requests and configuration
#Include conf/extra/httpd-info.conf

# Virtual hosts
#Include conf/extra/httpd-vhosts.conf

# Local access to the Apache HTTP Server Manual
#Include conf/extra/httpd-manual.conf

# Distributed authoring and versioning (WebDAV)
#Include conf/extra/httpd-dav.conf

# Various default settings
#Include conf/extra/httpd-default.conf

# Configure mod_proxy_html to understand HTML4/XHTML1
<IfModule proxy_html_module>
Include conf/extra/proxy-html.conf
</IfModule>

# Secure (SSL/TLS) connections
#Include conf/extra/httpd-ssl.conf
#
# Note: The following must must be present to support
#       starting without SSL on platforms with no /dev/random equivalent
#       but a statically compiled-in mod_ssl.
#
<IfModule ssl_module>
SSLRandomSeed startup builtin
SSLRandomSeed connect builtin
</IfModule>

Include conf/extra/proxy.conf
```

反向代理容器和 nextcloud 容器在同个 pod 内，把nextcloud 默认的 80 代理到了 443:

```bash
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so

<IfModule mod_proxy.c>
    ProxyPreserveHost On
    ProxyPass / http://localhost:80/
    ProxyPassReverse / http://localhost:80/
</IfModule>

LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
LoadModule ssl_module modules/mod_ssl.so
Include conf/extra/httpd-ssl.conf
```

在 `~/.config/containers/systemd/nextcloud.pod` 文件中，再把 443 映射到想要的端口（如9999），这样就可能在外网通过 SSL 访问 NextCloud 容器:

```bash

[Pod]
PodName=nextcloud
Network=bridge
PublishPort=9999:443

[Install]
WantedBy=default.target
```

## 参考资料

[ArchWiki: Certbot](https://wiki.archlinux.org/title/Certbot)
