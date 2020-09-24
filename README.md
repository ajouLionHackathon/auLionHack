# auLionHack

- clone 후 pip install -r requirements.txt로 패키지 설치
- 가상환경 업로드 하지 않도록 주의하기 (로컬에서 clone하는 폴더 위치와 동일한 곳에 가상환경 만들면 안 헷갈리고 좋음)
- 현재 project만 만든 상황 -> app 3개 (account, mainpage, trouble) 만들기 
- 로그인/회원가입은 일반 모델로 만들지 말고 Django에서 제공하는 Django Authentication 이용하기.<br>
로그인/회원가입 링크1 : [공식사이트](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Authentication)<br>
로그인/회원가입 링크2 : [초보몽키](https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-2/)
<br><br>
조만간 secret key 분리해야함. 이번주 안에 시행할 것임. [초보몽키](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)

---------------

#### Branch 할당
- master : 배포 브랜치<br>
- common : 공통적으로 변동하는 사항만 관리하는 브랜치 <br>
- mainpage : 메인페이지에 대해서 관리하는 브랜치 : 승욱, 호연<br>
- trouble : 고민글에 대한 브랜치 : 영윤, 유림, 규리<br>
- account : 로그인/회원가입에 대한 브랜치 : 소연<br>

#### Branch Rule
- 1. Pull Request 필요
- 2. 기본 브랜치(master,common,mainpage,trouble,account)에 대해서 바로 push 불가능, Pull Request에 지정한 Reviewer가 허용을 할 시에만 push 가능
- 3. master : 배포 브랜치이므로 모두의 작업이 끝났을 때 그제서야 merge시행할 것임. 



## Zenhub

수월한 브랜치와 커밋을 다루기 위해 젠허브를 사용할야. 어려움이 있더라도 잘 이해보도록하자..이해안되면 연락주세요

먼저 총 우리의 기본 브랜치는 master, common, account, trouble이렇게 네 가지 브랜치야.

 master은 절대 건들지말고 나머지 3개로만 사용할 꺼야. 

예를 들어서 지금 내가 리드미를 작성하고 있어. 리드미는 common 브랜치에서 작성해야겠지? 근데 common브랜치에 바로 커밋하고 푸쉬하는게 아니라 common 브랜치에서 하나의 브랜치를 또 생성하는거야. 

이 브랜치 생성기준을 젠 허브의 Epic을 기준으로 잡을꺼야. 이 리드미 작성을 에픽으로 만들면 아래와 같이 만들 수있어.

<img src="https://user-images.githubusercontent.com/49120090/94159105-24088180-febe-11ea-8f93-71c36cf94aa6.png" width="500" height="400">



그러면 젠허브에서는 아래와 같이 나올꺼야. 저 숫자 #1 보이지?? 얘를 브랜치 명으로 하고 얘는 하나의 작업이니까 커밋메시지도 동일하게 하도록할게.

<img src="https://user-images.githubusercontent.com/49120090/94159954-1bfd1180-febf-11ea-90aa-c98bf4986a3e.png" width="400" height="300">

![image-20200924234052750](/Users/uju_sy/Library/Application Support/typora-user-images/image-20200924234052750.png)

이런식으로..~! 

그리고 저렇게 브랜치를 파고 커밋까지 다 완료해서 하나의 에픽을 끝냈으면 해당 브랜치로 풀리퀘를 날려주면돼.

지금은 common 브랜치에서 했으니 #1->common으로 풀리퀘를 날려주면 되겠지??

끝났으니 풀리퀘를 해볼게.

이런식으로 Pull Requst 를 해줘.

![image](https://user-images.githubusercontent.com/49120090/94160614-c117ea00-febf-11ea-8ea1-1b3fb344d30f.png)

그 다음에 꼭 branch 지워주기.

![image](https://user-images.githubusercontent.com/49120090/94160924-2075fa00-fec0-11ea-8dc8-98ab373a14f5.png)



---------------

#### Templates 

* templates 을 앱 밖에다 만들고 그안에 앱이름 그안에 템플릿 넣어주시면 됩니다.!!
* Ex 

> templates
>
> > 앱이름
> >
> > 앱이름
> >
> > Trouble
> >
> > > write_Trouble.html
