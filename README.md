# JavaToPySo
Java JNI接口重写 调用python执行so文件
JavaToPySo--

          JavaToPySo.jar：Java JNI接口XXXFunction
                          JNI loadLibrary libJavaToPySo.so 文件前缀需要加lib 放于同文件夹或是java.library.path下
          callentelect.py：执行算法入口py 带参分割数组 并调用算法so
                            import os import sys 
                            argValue=sys.argv[1]
                            argValue = [ x.strip() for x in argValue.strip('[]').split(',') ]
          ent_elect_model.so：算法so（未成功打包静态库与算法依赖库 须部署py3环境与依赖库）

          PyToSo--
                    JavaToPySo.pyx：cython 接口
                    main.c：对 Cython 转换生成的代码 封装成 Java JNI 接口 重写JavaToPySo.pyx方法
                            接口函数前缀JNI_API_XXXFunction
                            JNI层面的参数jstring类型的转换
                            s.system("python3 callentelect.py 参数 ") 执行算法入口py

                    setup.py：JavaToPySo.pyx与main.c编译so 
                              须打包Java依赖、算法依赖库、py静态库
