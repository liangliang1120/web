## Nginx 
- 一个高性能的 HTTP 和反向代理服务器

## Nginx功能
- 反向代理：代理服务器。（正向代理是代理客户端）
- 负载均衡：Nginx提供的负载均衡策略有2种：内置策略和扩展策略。内置策略为轮询，加权轮询，Ip hash
- 动静分离

## Nginx优点
- 占有内存少
- 并发能力强

## Nginx常用命令
cd /usr/local/nginx/sbin/
./nginx  启动
./nginx -s stop  停止
./nginx -s quit  安全退出
./nginx -s reload  重新加载配置文件
ps aux|grep nginx  查看nginx进程

![image](https://user-images.githubusercontent.com/35073431/211252539-29415b35-bf64-4731-9eb0-3d695f794019.png)

https://www.kuangstudy.com/bbs/1353634800149213186
