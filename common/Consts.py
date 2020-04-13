class CommonData:
    # 用户变量
    username = "20171401108"
    password = "123456"
    orgId = 15
    token = ""
    host = "http://acv3.learn.it101.live"

    # 端口 get
    trends = "/api/courses/v3/trends" #获取最近学习动态
    courseList = "/api/courses/v3/myCourses" #获取课程列表
    recentLesson = "/api/learning/v3/129/recentLesson" #获取最近学习⼩节
    courseRole = "/api/courses/v3/129/courseRole/" #获取课程⻆⾊
    courseDetail = "/api/courses/v3/129/detail" #获取课程详情
    courseModules = "/api/courses/v3/129/modules/" #获取菜单
    courseChapters = "/api/courses/v3/129/chapters" #获取⼤纲
    chaperDetail = "/api/courses/v3/129/chapterDetail" #获取章节
    lesson = "/api/learning/v3/129/lesson/bu-quan-Java-cheng-xu" #获取⼩节详情
    # 端口 post
    studyTime = "/api/record/recordStudyTime/" #记录时间
    run = "/api/learning/v3/run" #运⾏
    judge = "/api/learning/v3/judge" #提交答案

    # post的payload
    studyTime_data = {"courseId":"129","lessonId":"bu-quan-Java-cheng-xu","duration":73317,"type":"lesson","beginAt":1586673558648,"url":"http://acv3.learn.it101.live/learning/129/bu-quan-Java-cheng-xu/"}
    run_data = {"courseId":"129","lessonId":"bu-quan-Java-cheng-xu","exerciseId":"5e43a01d4f503a0470aa7ec8","language":"java","code":"public  Program {\n    public static void  (String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}","stdin":""}
    judge_data = {"courseId":"129","exerciseType":"code-fill","lessonId":"bu-quan-Java-cheng-xu","exerciseId":"5e43a01d4f503a0470aa7ec8","code":"public  Program {\n    public static void  (String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}","blanks":[{"id":"5e43ca12ba961c91a0354700","answer":""},{"id":"5e43ca17ba961c91a0354701","answer":""}]}
