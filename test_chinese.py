import uroman as ur

uroman = ur.Uroman()


def test_bad_string():
    bad_string = "前三个月的focus的经营率的百分之多少或者是生命周期的focus经营率的百分之多少前者点位高一些或者点位低一些然后我们内部核算差不多这个点位应该是能擦过我们手臂的倍量就ok了这样所以我们我觉得没问题我觉得就这么写就是nre跟认证的费用是要在项目启动开始之前我要收到对吧然后关于倍量的成本的问题我们需要再拿到"
    romanized_bad_string = uroman.romanize_string(bad_string)
    assert romanized_bad_string
