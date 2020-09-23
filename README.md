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
<br>
#### Branch 할당
- master : 배포 브랜치
- common : 공통적으로 변동하는 사항만 관리하는 브랜치 
- mainpage : 메인페이지에 대해서 관리하는 브랜치 : 승욱, 호연
- trouble : 고민글에 대한 브랜치 : 영윤, 유림, 규리
- account : 로그인/회원가입에 대한 브랜치 : 소연

#### Branch Rule
- 1. Pull Request 필요
- 2. 기본 브랜치(master,common,mainpage,trouble,account)에 대해서 바로 push 불가능, Pull Request에 지정한 Reviewer가 허용을 할 시에만 push 가능
- 3. master : 배포 브랜치이므로 모두의 작업이 끝났을 때 그제서야 merge시행할 것임. 
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
