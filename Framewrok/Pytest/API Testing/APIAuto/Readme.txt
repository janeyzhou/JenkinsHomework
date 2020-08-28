Libary
request

Tips
cookies， header可以放入endpoint中
url可以放入配置文件或者api对应的方法中
每一api对应一个方法，api只返回response的内容，如果要处理response用另外的方法来处理
可以设置template-data，这样不用在input中输入全部字段，只需要输入测试字段就了
可以写方法获取template-data，input，output，casetitile，然后用方法处理temlate-data和input直接返回json样式，然后作为api方法的参数
将测试数据的获取，api，已经response的处理剥离开

Pytest

1. setup与范围
    def setup_class(self):

    def teardown_class(self):

    def setup_method(self):

    def teardown_method(self):

2. mark
    skip test case
    @pytest.mark.skip(condition='我就是要跳过这个用例啦')
    @pytest.mark.skipif(condition=1 < 2, reason='如果条件为true就跳过用例')

    mark 预期失败，执行成功/执行失败
    @pytest.mark.xfail(1 < 2, reason='预期失败， 执行失败')
    @pytest.mark.xfail(1 < 2, reason='预期失败， 执行成功')

    @pytest.mark.smoke: Run the test case as smoke test

3.  参数化
    input_list = ['iphone', 'huawei', 'hornor']
    output_list = ['goog'], 'very good', 'nice']
    d = [{"title": "test 1", "input":{}, "output":{}},
         {"title": "test 2", "input":{}, "output":{}},
         {"title": "test 3", "input":{}, "output":{}}]
    @pytest.mark.parametrize('input', input_list)
    def test(input)
    @pytest.mark.parametrize('input,output', [(input_list, output_list)])
    def test(input, output)
    @pytest.mark.parametrize('data', d)
    def test_api(data)
      print(data["title"])

4. Fixture
    fixture---test会找本文件中的fixture，如果没有会找conftest.py中的fixture；
    传fixture作为参数到test case中可以使用fixture返回的值，usefixture无法使用fixture的返回值，usefixture可以指定多个fixture，先调用的放在下面；
    @pytest.mark.usefixtures('test1')
    @pytest.mark.usefixtures('test2')

    如果是session级别的fixture需要放到conftest中；session级别的是可以跨多个.py的测试文件；module是当前的py测试文件有效
    FIXTURE  autouse=True---自动调用，不需要每个case去显示的调用
    @pytest.fixture(params=[])
    固件 ---pytest 会在执行测试函数之前（或之后）加载运行它们，最常见的可能就是数据库的初始连接和最后关闭操作，用户登录和退出
    Pytest 使用 yield 关键词将固件分为两部分，yield 之前的代码属于预处理，会在测试前执行；yield 之后的代码属于后处理，将在测试完成后执行。
    @pytest.fixture((scope='function/class/module/session'))
    def login():
        print('登录....')
    yield

    def test_index(login):
        print('主页....')

5.  conftest---一般放在根目录作为全局使用，并且要带一个__init__.py文件；也可以再不同的package写confest，只在package内部使用

6.  assert
    assert a=b, "check if a =b"
    assert "division by zero" in str("error message")
    assert xx 判断xx为真
    assert not xx 判断xx不为真
    assert a in b 判断b包含a
    assert a == b 判断a等于b
    assert a != b 判断a不等于b
    assert x > a  # 是否大于 a
    assert x < a  # 是否小于 a
    assert isinstance(x, dict)  # x 是否是 dict 类型
    assert 异常信息--比如确定这里一定要抛某种类型的异常，去assert这种异常有抛出
    def test_zero_division():
        with pytest.raises(ZeroDivisionError):
            1 / 0

7. 并发执行/覆盖率-pytest-cov/report-html/report-allure




