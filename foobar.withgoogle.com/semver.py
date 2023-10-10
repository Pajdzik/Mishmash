def solution(l):
    l.sort(cmp=sem_ver_comparison)
    return l


def sem_ver_comparison(ver1, ver2):
    major1, minor1, patch1, len1 = destruct_version(ver1)
    major2, minor2, patch2, len2 = destruct_version(ver2)

    if major1 > major2:
        return 1
    elif major1 < major2:
        return -1

    if minor1 > minor2:
        return 1
    elif minor1 < minor2:
        return -1
    elif minor1 == minor2 == 0:
        if len1 > len2:
            return 1
        elif len1 < len2:
            return -1

    if patch1 > patch2:
        return 1
    elif patch1 < patch2:
        return -1
    elif patch1 == patch2 == 0:
        if len1 > len2:
            return 1
        elif len1 < len2:
            return -1

    return 0


def destruct_version(v):
    parts = v.split('.')
    major = int(parts[0])
    minor = int(parts[1]) if len(parts) > 1 else 0
    patch = int(parts[2]) if len(parts) > 2 else 0

    return major, minor, patch, len(parts)


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
