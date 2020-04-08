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


 