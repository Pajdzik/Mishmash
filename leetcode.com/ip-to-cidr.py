class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def ip_to_number(ip: str) -> int:
            n_ip = 0
            blocks = [int(b) for b in ip.split(".")]

            for i in range(len(blocks)):
                n_ip <<= 8
                n_ip += blocks[i]

            return n_ip
        
        def number_to_ip(n_ip: int) -> str:
            res = []
            for _ in range(4):
                res.append(n_ip % (1 << 8))
                n_ip >>= 8

            res.reverse()
            return '.'.join([str(i) for i in res])
        
        def lowest_set_bit(n: int) -> int:
            for i in range(32):
                if (n & (1 << i)):
                    return i
            
            return 32
        
        number_ip = ip_to_number(ip)

        result = []
        while n > 0:
            lsb = lowest_set_bit(number_ip)
            mask = 1 << lsb
            while mask > n:
                mask //= 2
                lsb -= 1
            
            result.append([number_ip, 32 - lsb])
            n -= mask
            number_ip += mask

        return [f'{number_to_ip(r[0])}/{r[1]}' for r in result]


if __name__ == "__main__":
    Solution().ipToCIDR("255.0.0.7", 10)