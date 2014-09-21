"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        result = []
        pathList = path.split('/')
        for content in pathList:
            if content:
                if content == '..':
                    try:
                        result.pop()
                    except:
                        result = []
                elif content != '.':
                    result.append(content)
            print result
        return '/'+'/'.join(result)

solu = Solution()
print solu.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")
