

from toolsaf.main import Builder, TLS, DNS, HTTP, TCP, UDP, SSH

system = Builder.new("Zyxel NBG-418N v2")

any_host = system.any("Services")

router = system.device("Zyxel Router")
router.ip("192.168.1.1")

router_http = router / HTTP(auth=True, port=80)
router_https = router / TLS(port=443)
router_ssh = router / SSH(port=22)
router_dns = router / DNS
router_telnet = router / TCP(port=23)
router_upnp = router / TCP(port=5431)


router.hw("98:0D:67:AD:6B:7A")

router >> any_host / TLS / UDP(port=443) / HTTP 
any_host >> router / TLS / UDP(port=443) / HTTP 



if __name__ == '__main__':
    system.run()




