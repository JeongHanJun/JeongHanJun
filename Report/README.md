![Mando_logo_min](https://user-images.githubusercontent.com/54197360/143872651-5977e4f4-319d-4fd0-afd2-a05112606a24.png)
# Mando Internship
## 기간 : 2021.07.19 ~ 2021.12.31
### 위치 : 만도 중앙연구소 인턴 수행(판교 삼평동 위치)

![1_Mando_Introdution](https://user-images.githubusercontent.com/54197360/143871129-a1960127-bf8a-4502-90b0-9c1a026244b5.png)

### 소속 : SW Campus - SW 2 Lab - Software 3 team - ESTpart - ITPMS team

#### 주요 업무 개요

### 1. Auto Terrain Project
  - 차량 주행 실험 데이터를 Input으로 주어졌을때, 차량 주행 노면을 자동으로 분류할 수 있는 ML을 활용한 Automatical Classification Model 개발

![2_Autoterrain_CM](https://user-images.githubusercontent.com/54197360/143871265-4a6b8d8a-0344-4d6d-b8f3-0fa1c6e3967c.png)


### 2. IDB2 Master GE2 Project ASPICE 설계 - SW3 
    
    - EnterPrise Architecture를 활용하여 SW3 Component/Unit에 관한 설계작업
    
    - 28개의 Componet에 대하여 100여개의 Design 도식화


![3_EA](https://user-images.githubusercontent.com/54197360/143871318-45497e28-ce67-45f5-b36c-42479a30716c.png)

### 3. IDB2 GE2 UT 

    - SW3 동적 검증에 필요한 데이터 전처리 및 가공 작업
    
    - 16개의 Component, 32개의 헤더파일을 기반으로 약 400개의 tst파일 수정

![4_UT](https://user-images.githubusercontent.com/54197360/143871350-52da266c-4f82-4d22-ad45-4347299b2d51.png)





#### 1. AutoTerrain

##### 프로젝트 개요 및 목적

  
  - 현재 상용화된 노면 분류는 차량에 카메라 센서를 통해, 2D Image 를 통해 Computer Vision을 활용한 노면분류이다.
    
    
  - 하지만 위의 방법은 비용적인 측면, 유지 및 보수적인 측면, 카메라 센서 인식 의존성 문제(Black Ice) 등 단점이 존재하고, 상업화하기에는 더더욱 어려운 부분 존재한다.
    
    
  - 이를 해결하기 위해, 양산되는 신호 센서값들을 기반으로 Automatical Classification Model을 개발하여 위의 단점을 개선하고, 장점을 더욱 부각시키는 방향을 추진
    
    
  - 이를 해결하여 노면판단 관련하여 다양한 Insight와 방향성을 갖고, 시야를 확장하는 목적의 프로젝트 
    
      
# 

##### Input Data
  - Input Data는 2021년 1월 스웨덴 Winter Test 실험에서 취득한 데이터와, 2021년 8월 경기도 화성에 위치한 KATRI에서 실험을 통해 취득한 데이터
  - Winter Test 차량 주행 노면 : Asphalt, Snow, Ice, Split(좌/우 바퀴 노면 다른 부분) + Press 조절
  
  ![5_WinterTest_Track](https://user-images.githubusercontent.com/54197360/143871406-c18b5079-63ae-45d8-9898-88861bee1cb4.png)
    
      
      
  - KATRI Test 차량 주행 노면 : Asphalt, Gravel, Mud, Wide Low Friction, Wet Asphalt, Wet Gravel, Wet Mud, Wet Wide Low Friction + Press 조절
  
  ![6_KATRI_Track](https://user-images.githubusercontent.com/54197360/143871456-72a1224b-6ebb-438e-adbf-613ed4c66f74.png)
  
##### Features
  - Input Data는 1KHz / 100Hz 2가지 종류 존재.  
    
  - 프로젝트 목적과 방향성에 따라 100Hz 데이터를 학습에 사용
  
  - 100Hz Data Features
      - 9개 센서값 ( Speed, Lateral ACC, Longitudinal ACC, Yaw, EngineTq, EngineSpeed, BrkFlag, Steer )
  
  
![7_Data_columns](https://user-images.githubusercontent.com/54197360/143871499-f2886976-459e-451d-8661-1c4db680b430.png)
    
  

##### Data Preprocessing / Labeling
  - CANape를 이용해 영상 data와 신호 data 싱크 조율, 주행이라고 판단되기 힘든 부분 삭제, 특이사항 확인
    
    ![8_CANape](https://user-images.githubusercontent.com/54197360/143871534-4e2a560d-23f7-45f6-a801-75fb9b3d7569.png)
      
  - 영상 편집 프로그램을 이용해 Data 편집 및 싱크 조율  
  - Matlab을 통해 MDF to CSV
  - 카메라 센서를 통해 확인한 Label을 Python을 통해 Data에 입력


##### Basic Process
  - load Data -> Data Preprocessing -> Train -> Test
![9_Model_Basic](https://user-images.githubusercontent.com/54197360/143871569-99f7b201-685b-4328-9e39-5747927648f2.png)


##### Model Train Process & Structure
  - Train Process in ML
  ![10_Model_Train_Process](https://user-images.githubusercontent.com/54197360/143871609-206be490-0f90-48fb-9216-132cadca3533.png)
  - ML model Structure
  ![11_ML_Model_Structure](https://user-images.githubusercontent.com/54197360/143871645-8af6d16b-c421-43fa-92e7-bcc3b6ee1334.png)
 

##### Feature Importance
  - 모델 학습에 있어서 어떤 Feature가 가장 중요한가? - Premutation Importance
  - 모델에서 클래스별 분류할 때 어떤 Feature가 가장 큰 기여를 하였는가? - Feature Importance
  ![12_Feature_Importance](https://user-images.githubusercontent.com/54197360/143871669-e9f16e88-1207-4d59-b251-08f4e6d31e09.png)
  


#### Monthly Result
  - 7,8,9월에는 학습 데이터 취득, 데이터 전처리 및 가공, DB구축, 학습 네트워크 설계등의 작업수행
  - 10월에는 Low Mu Classification에서 평균 91% , 최고 92% 정확도 성능의 모델 보유
  - 11월에는 High Mu + Low Mu classification에서 평균 95%, 최고 98% 정확도 성능의 모델 보유
  ![13_Montly_Result](https://user-images.githubusercontent.com/54197360/143871713-73388225-5f32-4311-aae1-39a3afde6fd9.png)



#### 동향조사와의 비교
  - 본 프로젝트만이 가진, 타 기업 및 대학원에서의 연구과제들과 차별화된 점
      - 다양한 노면 분류
          - 다른 연구과제들에서는 Dry 노면, 대부분 6개 미만의 노면들을 분류하지만, 본 프로젝트는 Wet 노면을 포함하여 총 11개의 노면 분류
          - 본 프로젝트의 Split 노면은 좌/우측 타이어 노면이 Asphalt/Ice 혹은 Ice/Asphalt인 노면으로 , 해당 노면도 분류
      - 카메라 센서 사용하지 않음
          - 2차원 이미지 데이터를 기반으로 한 다른 과제들과 달리, 양산되는 센서값만으로 노면판단 및 분류
      - 다양한 노면 데이터에 대한 실험 데이터 취득
          - 한국의 KATRI 데이터, 스웨덴의 Winter Test Data로 한 환경에 치우쳐진 데이터가 아니라, 다양한 환경에서의 실험 데이터 사용
          - 이로인해, 학습데이터의 질이 우수하다. 모델의 첫 정확도가 87% 였다는 점, 다른 모델들보다 약 10% 이상 높다는 점이 이를 증명함.

#### 결론
  - 모든 노면에 대하여 큰 편차 없이 만족할만한 수준의 분류 성능 모델 확보
  - 학습 데이터의 중요성에 대해 다시 한번 느낌
      - 본 프로젝트의 문제점 中 대부분은 Data Dependency 혹은 Overfitting 관련 내용이었고, 이를 해결하는 과정에서 모델 학습 Data의 중요성을 체감함
  - 틀린 예측에 대한 데이터들에 대한 insight 및 분석 필요
      - 211129 기준
        -  틀린 예측과 맞는 예측 데이터들의 분석, 비교 및 시각화
        -  시간축 단위로 Test 진행하여 실제로 차량 주행 실험과 함께 학습 결과를 받을 수 있는 환경 조성 

### 2. IDB2 Master GE2  ASPICE Project
- ASPICE : Automotive Software Process Improvement and Capability dEtermination  

    - 자동차 SW 개발 프로세스 및 관련 비즈니스 관리 기능 전반
    
    - 완성 차 업체에 부품을 공급하는 공급업체 능력 평가, 평가결과를 공식적으로 등급화 → 공급업체의 품질 능력 향상!
    
    - 기본 산출물  
     
         - SW Requirement
             - 말그대로 요구사항 관련 : 신규 추가 항목, Interface, Traceability, 주의사항, Feature, 검증 기준, Release / Test 단계 등  
             
         - SW Architecture Design (SAD)
             - SW 구조 설계 관련 : Component간 동적 흐름 기술, Unit 단위 Sequence diagram, Interface, dependency, data dictionary 등  
             
         - SW Unit Design (SUD)
             - SW Unit 설계 관련 : Unit Traceaility, 문서/File 구조, Interface, static diagram, data flow, call tree , description 등  
             
         - SW Source Code
             - SW 소스코드를 통한 구현 :.c / .h 등의 코드 결과물 , 협업을 위한 주석 (comment) 
             
         - SW Qualification Test (SWQT)
             - SW 검증 및 테스트 관련 : Precondition, Test Procedure, Expected result , Test result , Trace Status 등  
             
         - SW Integration & Integration Test (SWIT)
             - SW 통합 테스트 및 report 관련 : RJ SW 수행 결과, 일정, Test Case/Report PTC 등록 전략, Traceability 등
             
         - SW Unit verification (SWUT)
             - SW 유닛 테스트 결과 및 report 관련 : SK3 SW 수행 결과, 일정, Test Case/Report PTC 등록 전략, Traceability 등
# 



- IDB2 SWE.2 Behavior Design
    - 위 기본 산출물 中 SAD에 해당
    - 각 SW Feature(ABS, AVH, ACC, ETCS 등)별로 수행 가능 시나리오를 Component(WSLC, ABC, SSM 등)간 Sequence Diagram으로 작성한 것
    - 동작모드(Normal/Safe/Shutdown mode), 제어/비제어상황, 기능저하/기능금지상황 별 작성 필요하나 우선적으로 Normal 동작모드 최소 1개이상 필요
    - 각 Component는 하나 이상의 unit으로 구성된다.
    - 각 Compoent 들의 Behavior Design에는 연결성 및 의존성 여부 포함된 상태 유지, 추가적인 설명은 comment or Data Dictionary 참고 
    - 최종 산출물인 SW Behavior Design, Interface 자료, SW Architecture Design은 서로 일치한다.
    ![14_Behavior_Designs](https://user-images.githubusercontent.com/54197360/143871744-afd4fa83-057a-4cc4-867d-c1bae866c1dc.png)
        
#    
  - IDB2 SWE.2 Static Design
      - 위 기본 산출물 中 SUD에 해당
      - SAD에서 SW element를 파악한다. 여기서 element는 설계 수준에 따라 component 또는 unit이 될 수 있다.
      - SW element에 할당된 SW Requirement를 확인하여, 제공할 기능 및 만족할 속성을 이해한다.
      - SAD에 정의된 Behavior Design, component dependency, interface design을 토대로 elemenet 사이 관계와 interface를 이해한다.
      - 위에 따라 SW Component(ABS, BTA, SSM 등) 예하의 Unit들(ACC, FBC, AVH 등)간 관계를 Static Diagram으로 작성한 것
      - 최종 산출물인 SW Unit Design specification , Interface 자료,  SW Unit Design은 서로 일치한다.
      ![15_Static_Design](https://user-images.githubusercontent.com/54197360/143872028-b36e6b68-7b7b-43dc-b603-6ff4cc42dbc7.png)
# 

  - IDB2 SWE.2 Dynamic Design
      - 위 기본 산출물 中 SUD에 해당
      - SW element 파악은 위의 Static Design과 동일
      - SW element에 할당된 SW Requirement를 확인하여, 함수간에 correlation과 internal functions를 이해한다.
      - 위에 정의된 자료들을 토대로 elemenet 간에 hierarchy와 interface, Global Variable, Structure를 이해한다.
      - 위에 따라 SW Component(ABS, BTA, SSM 등) 예하의 Unit들(ACC, FBC, AVH 등)간 Interaction을 Dynamic Diagram으로 작성한 것
      - 최종 산출물인 SW Unit Design specification , Interface 자료,  SW Unit Design은 서로 일치한다.
      ![16_Dynamic_Design](https://user-images.githubusercontent.com/54197360/143872062-edc34f9a-6d4a-4b3c-9cf1-b40a0cd8f054.png)

### IDB2 GE2 SWUT
- SW Unit Test 동적 검증을 위해 데이터 가공 및 전처리
    - 컴포넌트 명, 구조체 변수명은 IDB1(Before)과 IDB2(After)의 헤더파일과 tst파일의 비교로 확인
    ![17_UT_Edit](https://user-images.githubusercontent.com/54197360/143872092-c7689567-c2f5-4103-b38e-e411de3b675a.png)
    - IDB1(Before)과 IDB2(After)의 컴포넌트 내 RTE 구조체 변수, 멤버 변수, 변수 Type , 동적 할당 여부 , 명칭에 의존적인 부분을 제외 등을 고려 하여 tst 파일 내 대응되는 RTE 변수 수정
    - 16개의 Component에 대해 400여개의 tst 파일에서 3만5천개의 변수 수정
    ![18_UT_Edit_list](https://user-images.githubusercontent.com/54197360/143872118-909a8a70-65d5-4151-8053-4f57a96ad013.png)
    - 수정된 tst 파일을 기반으로 VectorCast로 동적 검증


```python

```
