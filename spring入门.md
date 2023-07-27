# spring 日记第一节

## main文件的@SpringBootApplication注释

里面有扫描bean的功能,加上controller之类的注解就能被扫描到


@Service 用于标注业务层组件

@Controller 用于标注控制层组件

@Repository 用于标注数据访问组件，即DAO组件

@Component 泛指组件，当组件不好归类的时候，我们可以使用这个注解进行标注

```java 
@Repository
public class AlphaDaoMybatis implements  AlphaDao{

    @Override
    public String select() {
        return "Mybatis";
    }
}
```
## 理解dao接口 javabean的运用

接口中写方法

bean里写实现方式 面向接口编程思路

这样易于更新功能 比如对数据库的访问可以由hibernate更新为mybatis