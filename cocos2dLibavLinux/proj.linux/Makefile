CC      = gcc
CXX     = g++
TARGET	= HelloCpp
CCFLAGS = -Wall
CXXFLAGS = -Wall
VISIBILITY = 

COCOS2DX_PATH = /home/liyong/gameEngine/cocos2d-x/cocos2dx
COCOS2DX_PATH_2 = /home/liyong/gameEngine/cocos2d-x
INCLUDES =  -I../ \
			-I../Classes \
			-I$(COCOS2DX_PATH) \
			-I$(COCOS2DX_PATH)/platform/third_party/linux \
			-I$(COCOS2DX_PATH)/platform/third_party/linux/libfreetype2 \
			-I$(COCOS2DX_PATH)/cocoa \
			-I$(COCOS2DX_PATH)/include \
			-I$(COCOS2DX_PATH)/platform \
			-I$(COCOS2DX_PATH)/platform/linux \
			-I$(COCOS2DX_PATH)/kazmath/include \
			-I$(COCOS2DX_PATH)/platform/third_party/linux/libxml2 \
			-I$(COCOS2DX_PATH)/platform/third_party/linux/libjpeg 


DEFINES = -DLINUX

OBJECTS = ./main.o \
        ../Classes/AppDelegate.o \
        ../Classes/HelloWorldScene.o \
        ../Classes/Lightning.o \
        ../Classes/Bomb.o \
        ../Classes/Cannon.o \
        ../Classes/Background.o \
        ../Classes/Range.o \
        ../Classes/MapGrid.o \
		../Classes/VideoController.o \
		../Classes/yuv420.o 

LBITS := $(shell getconf LONG_BIT)
ifeq ($(LBITS),64)
STATICLIBS_DIR = $(COCOS2DX_PATH)/platform/third_party/linux/libraries/lib64
else
STATICLIBS_DIR = $(COCOS2DX_PATH)/platform/third_party/linux/libraries
endif
STATICLIBS = 
STATICLIBS = $(STATICLIBS_DIR)/libfreetype.a \
				$(STATICLIBS_DIR)/libxml2.a \
				$(STATICLIBS_DIR)/libpng.a \
				$(STATICLIBS_DIR)/libjpeg.a \
				$(STATICLIBS_DIR)/libtiff.a \
#				$(STATICLIBS_DIR)/libGLEW.a \

SHAREDLIBS = 

ifeq ($(LBITS),64)
SHAREDLIBS_DIR = $(COCOS2DX_PATH_2)/CocosDenshion/third_party/fmod/lib64/api/lib
SHAREDLIBS = -L$(SHAREDLIBS_DIR) -lfmodex64
else
SHAREDLIBS_DIR = $(COCOS2DX_PATH_2)/CocosDenshion/third_party/fmod/api/lib
SHAREDLIBS = -L$(SHAREDLIBS_DIR) -lfmodex
endif

SHAREDLIBS += -lopencv_core -lopencv_highgui
SHAREDLIBS += -lglfw 
#SHAREDLIBS += -L../../../../lib/linux/Debug -lcocos2d -lrt -lz -lcocosdenshion -Wl,-rpath,../../../../../lib/linux/Debug/ 
SHAREDLIBS += -Wl,-rpath,../../$(SHAREDLIBS_DIR)
#SHAREDLIBS += -Wl,-rpath,../../../../../cocos2dx/platform/third_party/linux/glew-1.7.0/glew-1.7.0/lib
SHAREDLIBS += -L$(COCOS2DX_PATH)/platform/third_party/linux/glew-1.7.0/glew-1.7.0/lib -lGLEW
SHAREDLIBS += -Wl,-rpath,$(COCOS2DX_PATH)/platform/third_party/linux/glew-1.7.0/glew-1.7.0/lib

#$(shell ../../build-linux.sh $<)

BIN_DIR_ROOT=bin
BIN_DIR = $(BIN_DIR_ROOT)

debug: BIN_DIR = $(BIN_DIR_ROOT)/debug
debug: CCFLAGS += -g3 -O0
debug: CXXFLAGS += -g3 -O0 -D__STDC_CONSTANT_MACROS
debug: SHAREDLIBS += -L$(COCOS2DX_PATH_2)/lib/linux/Debug -lcocos2d -lrt -lz -lcocosdenshion -lavcodec -lavformat -lswscale
debug: SHAREDLIBS += -Wl,-rpath,$(COCOS2DX_PATH_2)/lib/linux/Debug/
debug: SHAREDLIBS += -Wl,-rpath,./lib
debug: DEFINES += -DDEBUG -DCOCOS2D_DEBUG=1
debug: $(TARGET)


release: BIN_DIR = $(BIN_DIR_ROOT)/release
release: CCFLAGS += -O3
release: CXXFLAGS += -O3  -D__STDC_CONSTANT_MACROS
release: SHAREDLIBS += -L../../../../lib/linux/Release -lcocos2d -lrt -lz -lcocosdenshion
release: SHAREDLIBS += -Wl,-rpath,../../../../../../lib/linux/Release/
release: DEFINES += -DNDEBUG
release: $(TARGET)

####### Build rules
$(TARGET): $(OBJECTS) 
	mkdir -p $(BIN_DIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) $(DEFINES) $(OBJECTS) -o $(BIN_DIR)/$(TARGET) $(SHAREDLIBS) $(STATICLIBS)

####### Compile
%.o: %.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) $(DEFINES) $(VISIBILITY) -c $< -o $@

%.o: %.c
	$(CC) $(CCFLAGS) $(INCLUDES) $(DEFINES) $(VISIBILITY) -c $< -o $@
    

clean: 
	rm -f $(OBJECTS) $(TARGET) core
