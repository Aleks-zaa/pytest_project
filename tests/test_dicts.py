from utils import dicts


def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == 'mercurial'
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", "git") == 'mercurial'
    assert dicts.get_val({}, "vcs", 'git') == 'git'
    assert dicts.get_val({}, "vcs", 'bazaar') == 'bazaar'
#
# >>> data = {"vcs": "mercurial"}
# >>> get_val(data, "vcs")
# 'mercurial'
# >>> get_val(data, "vcs", "git")
# 'mercurial'
# >>> data = {}
# >>> get_val({}, "vcs", "git")
# 'git'
# >>> get_val({}, "vcs", "bazaar")
# 'bazaar'