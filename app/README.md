### 简介:
Flask-RESTful 是一个 Flask 扩展插件，它添加了快速构建 REST APIs 的支持。是能够跟你现有的ORM/库协同工作的轻量级的扩展。

add_argument可以指定这个字段的名字，这个字段的数据类型等
fault：默认值，如果这个参数没有值，那么将使用这个参数指定的值。
required：是否必须。默认为False，如果设置为True，那么这个参数就必须提交上来。
type：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。
choices：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。
help：错误信息。如果验证失败后，将会使用这个参数指定的值作为错误信息。
trim：是否要去掉前后的空格。
location：指定参数的位置。
 如果你要接受一个键有多个值的话，你可以传入 action='append'：

```
    :param name: Either a name or a list of option strings, e.g. foo or
        -f, --foo.
    :param default: The value produced if the argument is absent from the
        request.
    :param dest: The name of the attribute to be added to the object
        returned by :meth:`~reqparse.RequestParser.parse_args()`.
    :param bool required: Whether or not the argument may be omitted (optionals
        only).
    :param action: The basic type of action to be taken when this argument
        is encountered in the request. Valid options are "store" and "append".
    :param ignore: Whether to ignore cases where the argument fails type
        conversion
    :param type: The type to which the request argument should be
        converted. If a type raises an exception, the message in the
        error will be returned in the response. Defaults to :class:`unicode`
        in python2 and :class:`str` in python3.
    :param location: The attributes of the :class:`flask.Request` object
        to source the arguments from (ex: headers, args, etc.), can be an
        iterator. The last item listed takes precedence in the result set.
    :param choices: A container of the allowable values for the argument.
    :param help: A brief description of the argument, returned in the
        response when the argument is invalid. May optionally contain
        an "{error_msg}" interpolation token, which will be replaced with
        the text of the error raised by the type converter.
    :param bool case_sensitive: Whether argument values in the request are
        case sensitive or not (this will convert all values to lowercase)
    :param bool store_missing: Whether the arguments default value should
        be stored if the argument is missing from the request.
    :param bool trim: If enabled, trims whitespace around the argument.
    :param bool nullable: If enabled, allows null value in argument.
 ```

输出字段：
对于一个视图函数，你可以指定好一些字段用于返回。以后可以使用ORM模型或者自定义的模型的时候，他会自动的获取模型中的相应的字段，生成json数据，然后再返回给客户端。这其中需要导入flask_restful.marshal_with装饰器。并且需要写一个字典，来指示需要返回的字段，以及该字段的数据类型。示例代码如下：

class ProfileView(Resource):
    resource_fields = {
        'username': fields.String,
        'age': fields.Integer,
        'school': fields.String
    }

    @marshal_with(resource_fields)
    def get(self,user_id):
        user = User.query.get(user_id)
        return user
在get方法中，返回user的时候，flask_restful会自动的读取user模型上的username以及age还有school属性。组装成一个json格式的字符串返回给客户端。

重命名属性：

很多时候你面向公众的字段名称是不同于内部的属性名。使用 attribute可以配置这种映射。比如现在想要返回user.school中的值，但是在返回给外面的时候，想以education返回回去，那么可以这样写：

resource_fields = {
    'education': fields.String(attribute='school')
}
默认值：

在返回一些字段的时候，有时候可能没有值，那么这时候可以在指定fields的时候给定一个默认值，示例代码如下：

resource_fields = {
    'age': fields.Integer(default=18)
}
复杂结构：

有时候想要在返回的数据格式中，形成比较复杂的结构。那么可以使用一些特殊的字段来实现。比如要在一个字段中放置一个列表，那么可以使用fields.List，比如在一个字段下面又是一个字典，那么可以使用fields.Nested。以下将讲解下复杂结构的用法：

class ProfileView(Resource):
    resource_fields = {
        'username': fields.String,
        'age': fields.Integer,
        'school': fields.String,
        'tags': fields.List(fields.String),
        'more': fields.Nested({
            'signature': fields.String
        })
    }
 


