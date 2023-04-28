class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.replace("//", "/")

        pathArr = path.split("/")
        if pathArr[-1] == '':
            pathArr[:] = pathArr[:-1]

        needUp = 0
        canonicalPath = []

        for i in range(len(pathArr) - 1, -1, -1):
            tempStr = pathArr[i]
            if tempStr == "..":
                needUp += 1
            elif tempStr == ".":
                continue
            elif tempStr != "":
                if needUp == 0:
                    canonicalPath.insert(0, tempStr)
                else:
                    needUp -= 1
            else:
                continue

        return '/' + '/'.join([str(elem) for elem in canonicalPath])



path1 = "/home/"
path2 = "/../"
path3 = "/home//foo/"
path4 = "/a/./b/../../c/"
path5 = "/a/../../b/../c//.//"
path6 = "/a//b////c/d//././/.."
path7 = "/home/foo/.ssh/../.ssh2/authorized_keys/"

print(Solution().simplifyPath(path1))
print(Solution().simplifyPath(path2))
print(Solution().simplifyPath(path3))
print(Solution().simplifyPath(path4))
print(Solution().simplifyPath(path5))
print(Solution().simplifyPath(path6))
print(Solution().simplifyPath(path7))