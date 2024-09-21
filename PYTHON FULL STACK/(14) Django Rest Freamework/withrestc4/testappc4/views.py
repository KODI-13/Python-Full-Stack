from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testappc4.models import Employee
from testappc4.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from testappc4.permissions import IsReadOnly, IsGetOrPatch, DeepakPermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from testappc4.authentications import CutomAuthenticatation, CutomAuthenticatation2

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [TokenAuthentication,]           # token authentication can added locally like these
    # authentication_classes = [JSONWebTokenAuthentication,]    # *NOTE = JWT Authentication is not working plz chck it in new project  
    # authentication_classes = [CutomAuthenticatation,]
    authentication_classes = [CutomAuthenticatation2,]          # key for Deepak user in this url http://127.0.0.1:8000/api/1/?username=Deepak&key=k2Z1D84
    permission_classes = [IsAuthenticated,]                                     # but each CBV need to add it so wew can use misins concept, and inhert it with mixin class
    # permission_classes = [AllowAny,]                                            # but each CBV need to add it so wew can use misins concept, and inhert it with mixin class
    # permission_classes = [IsAdminUser,]                                         # but each CBV need to add it so wew can use misins concept, and inhert it with mixin class
    # permission_classes = [IsAuthenticatedOrReadOnly,]                           # but each CBV need to add it so wew can use misins concept, and inhert it with mixin class
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]                # but each CBV need to add it so wew can use misins concept, and inhert it with mixin class
    # permission_classes = [IsReadOnly,]                                          # but each CBV need to add it so wew can use misins concept, and inhert it with mixin class
    # permission_classes = [IsGetOrPatch,]       
    # permission_classes = [DeepakPermission,]             



"""
token authentication -->
two ways to add token authentication
1) locally -->
                token authentication can added locally like above
                but each CBV need to add it so wew can use misins concept, and inhert it with mixin class

2) Globally --> 
                inside settings.py
                REST_FRAMEWORK = {
                    'DEFAULT_AUTHENTICATION_CLASSES' : ('rest_framework.authentication.TokenAuthentication',),
                    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',)
                }

*NOTE = Global authentication can be override by local authentication

======================================================================================================================================================================================================

IsAuthenticated --> only Authenticated person perform all operations
                    permission_classes = [IsAuthenticated, ] 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

AllowAny --> when there are multiply classes availble and all of them having global authentication but if we want to disable authentication for perticular class then we can use AllowAny
               permission_classes = [AllowAny, ]  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
IsAdminUser --> only admin can perform all operation    (to create admin we have to enable staff status in the django admin section for that perticular user)
                permission_classes = [IsAdminUser, ] 

there are 3 types of user
normal user --> can not access admin section
admin --> can login into admin section but cant have permission to see whats in the admin section
superuser --> can login into admin section and can modify anything
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

IsAuthenticatedOrReadOnly --> it has two parts -->
                                                Read Only operations --> GET, HEAD, OPTIONS
                                                IsAuthenticated operation --> POST, PUT, PACTH, DELETE (All write operations) and GET, HEAD, OPTIONS (All Read Operations)
                              permission_classes = [IsAuthenticatedOrReadOnly, ] 
                            
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

djangoModelPermission --> to access end point authentication must be required(token)......it is basic point
                          to perform operations in djangoModelPermission
                          GEt --> authentication is enough model permissions are not required
                          POST, PUT, PATCH, DELETE --> Authentication + Model Permissions

                          model permission --> 
                                               POST --> add model permisssion
                                               PUT, PATCH --> change model permission
                                               DELETE --> delete model permission

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

djangoModelPermissionOrAnonReadOnly --> to access end point authentication must be required(token)......it is basic point
                          to perform operations in djangoModelPermission
                *NOTE     GEt --> authentication is not required and model permissions are not required ...Any anonumous person can access it without authentication
                          POST, PUT, PATCH, DELETE --> Authentication + Model Permissions

                          model permission --> 
                                               POST --> add model permisssion
                                               PUT, PATCH --> change model permission
                                               DELETE --> delete model permission

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                               
custom permission classes --> our own perrmission classes
                            
                              class XYZPermission(BasePermission):          it is neccessary to be child class of BasePermission
                                    def has_perrmission(self, request, view):   we have to override has_permission method
"""



"""
Token authentication --> performance problems
                         scalability problems       cause whenever partner application send request with token then our django 
                                                          django application communicate with database for validating that token
                                                          and also thihs token dosent give info of user 
                                                          we explicitly query the database in order to get info of user

that's why we goin to use 3rd party authentication mechanisms

JWT (json web token) authentication --> this token gives info about user we dont have to commuicate with database
                                        for every request we dont have to communicate with database in order to validate tken

there are several packages available to implement jwt in DRF
for e.g. djangorestframework-jwt........pip install djangorestframework-jwt
         django-rest-framework-simplejwt

steps -->
        1) acceess token --> 5 min access time ..after this it will expired ... this type of setting in order to provide security
        2) refresh token --> before expiring token renewal of tokwn
                             for e.g. there is access token for 5 min
                                      and after 4 min you realized that you need this for more time
                                      so u asked for new token then it eill create new token using old token and that token will be provided

                            after genrating new token , old token is accessable
                            non-expired tokens can be 'refreshed' to obtain a brand new token with renewed expiration time 
                            refreshing capability only 7 daya
                            some special arrragement we should do in settings.py

        3) verify token --> if token is valid it will provide 200 status code and same toekn will be returned
                            it it is not valid then 400 status code with clear reason provided

to genarate accesss token : username and password required + db communication reuired
to refresh access token : exisiting token

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

custom permission classes --> our own Authentication classes
                            
                              class CustomAuthenticataction(BaseAuthenticatation):          it is neccessary to be child class of BaseAuthenticatation
                                    def authenticate(self, request):   we have to override authenticate method
                                        if successful authentication:
                                            return tuple(user,None)
                                        else:
                                            raise AuthenticationFailed Exception
"""