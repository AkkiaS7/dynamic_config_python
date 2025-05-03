# WIP: Still under development/项目仍在开发中

# Usage/使用方式

1. Clone the repository as a submodule in your project:  
   将本仓库作为子模块克隆到你的项目中：

   ```bash
   git submodule add https://github.com/AkkiaS7/dynamic_config_python.git dynamic_config
   ```

2. Add Demo config in os environment:    
   在系统环境变量中添加演示配置：
    ```bash
    export TEXT_TO_SAY_CONF="hellow world by os env!"
    export BOOL_CONF_1=True # True/true/1
    export BOOL_CONF_2=0    # False/false/0
    export 'DICT_CONF={"key1": "value1", "key2": "value2"}'
    export 'LIST_CONF=["item1", "item2", "item3"]'
    export 'PYDANTIC_BASE_MODEL_CONF={"name":"AkkiaS7"}'
    ```
   

3. import and use it in your code:  
    在你的代码中导入并使用：
    ```python
    from dynamic_config import conf
    text_to_say = conf.get_conf("TEXT_TO_SAY_CONF", "hello world")
    print(text_to_say) # hellow world by os env!
    
    # Bool
    bool_conf_1 = conf.get_conf("BOOL_CONF_1", False)
    print(bool_conf_1) # True
    print(isinstance(bool_conf_1, bool)) # True
    bool_conf_2 = conf.get_conf("BOOL_CONF_2", True)
    print(bool_conf_2) # False
    print(isinstance(bool_conf_2, bool)) # True

    # Dict
    dict_conf = conf.get_conf("DICT_CONF",{})
    print(dict_conf) # {'key1': 'value1', 'key2': 'value2'}
    print(isinstance(dict_conf, dict)) # True
    
    # List
    list_conf = conf.get_conf("LIST_CONF", [])
    print(list_conf) # ['item1', 'item2', 'item3']
    print(isinstance(list_conf, list)) # True
    
    # Pydantic BaseModel
    from pydantic import BaseModel
    class MyModel(BaseModel):
        name: str = "unknown"
    my_model_conf = conf.get_conf("PYDANTIC_BASE_MODEL_CONF", MyModel)
    print(my_model_conf) # MyModel(name='AkkiaS7')
    print(isinstance(my_model_conf, MyModel)) # True
    ```
