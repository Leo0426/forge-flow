# 深模块

来自《A Philosophy of Software Design》：

**深模块** = 小接口 + 大量实现

```

   Small Interface     ← 少量方法，简单参数

                     
                     
  Deep Implementation  ← 隐藏复杂逻辑
                     
                     

```

**浅模块** = 大接口 + 少量实现（避免）

```

       Large Interface             ← 很多方法，复杂参数

  Thin Implementation              ← 只是透传

```

设计接口时，询问：

- 我能减少方法数量吗？
- 我能简化参数吗？
- 我能在内部隐藏更多复杂性吗？
