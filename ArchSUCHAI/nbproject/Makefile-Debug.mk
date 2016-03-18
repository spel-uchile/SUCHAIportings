#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Environment
MKDIR=mkdir
CP=cp
GREP=grep
NM=nm
CCADMIN=CCadmin
RANLIB=ranlib
CC=gcc
CCC=g++
CXX=g++
FC=gfortran
AS=as

# Macros
CND_PLATFORM=GNU-Linux
CND_DLIB_EXT=so
CND_CONF=Debug
CND_DISTDIR=dist
CND_BUILDDIR=build

# Include project Makefile
include Makefile

# Object Directory
OBJECTDIR=${CND_BUILDDIR}/${CND_CONF}/${CND_PLATFORM}

# Object Files
OBJECTFILES= \
	${OBJECTDIR}/OS_calls/Arch/posix/p_console.o \
	${OBJECTDIR}/OS_calls/Arch/posix/p_file.o \
	${OBJECTDIR}/OS_calls/Arch/posix/p_gnrlcalls.o \
	${OBJECTDIR}/OS_calls/Arch/posix/p_queue.o \
	${OBJECTDIR}/OS_calls/Arch/posix/p_tasks.o \
	${OBJECTDIR}/System/RepoCmd/cmdCON.o \
	${OBJECTDIR}/System/Tasks/taskConsole.o \
	${OBJECTDIR}/System/cmdRepository.o \
	${OBJECTDIR}/System/dataRepository.o \
	${OBJECTDIR}/System/stateRepository.o \
	${OBJECTDIR}/System/suchaiDeployment.o \
	${OBJECTDIR}/System/taskDispatcher.o \
	${OBJECTDIR}/System/taskExecuter.o \
	${OBJECTDIR}/main.o


# C Compiler Flags
CFLAGS=

# CC Compiler Flags
CCFLAGS=
CXXFLAGS=

# Fortran Compiler Flags
FFLAGS=

# Assembler Flags
ASFLAGS=

# Link Libraries and Options
LDLIBSOPTIONS=

# Build Targets
.build-conf: ${BUILD_SUBPROJECTS}
	"${MAKE}"  -f nbproject/Makefile-${CND_CONF}.mk ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/archsuchai

${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/archsuchai: ${OBJECTFILES}
	${MKDIR} -p ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}
	${LINK.c} -o ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/archsuchai ${OBJECTFILES} ${LDLIBSOPTIONS}

${OBJECTDIR}/OS_calls/Arch/posix/p_console.o: OS_calls/Arch/posix/p_console.c 
	${MKDIR} -p ${OBJECTDIR}/OS_calls/Arch/posix
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/OS_calls/Arch/posix/p_console.o OS_calls/Arch/posix/p_console.c

${OBJECTDIR}/OS_calls/Arch/posix/p_file.o: OS_calls/Arch/posix/p_file.c 
	${MKDIR} -p ${OBJECTDIR}/OS_calls/Arch/posix
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/OS_calls/Arch/posix/p_file.o OS_calls/Arch/posix/p_file.c

${OBJECTDIR}/OS_calls/Arch/posix/p_gnrlcalls.o: OS_calls/Arch/posix/p_gnrlcalls.c 
	${MKDIR} -p ${OBJECTDIR}/OS_calls/Arch/posix
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/OS_calls/Arch/posix/p_gnrlcalls.o OS_calls/Arch/posix/p_gnrlcalls.c

${OBJECTDIR}/OS_calls/Arch/posix/p_queue.o: OS_calls/Arch/posix/p_queue.c 
	${MKDIR} -p ${OBJECTDIR}/OS_calls/Arch/posix
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/OS_calls/Arch/posix/p_queue.o OS_calls/Arch/posix/p_queue.c

${OBJECTDIR}/OS_calls/Arch/posix/p_tasks.o: OS_calls/Arch/posix/p_tasks.c 
	${MKDIR} -p ${OBJECTDIR}/OS_calls/Arch/posix
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/OS_calls/Arch/posix/p_tasks.o OS_calls/Arch/posix/p_tasks.c

${OBJECTDIR}/System/RepoCmd/cmdCON.o: System/RepoCmd/cmdCON.c 
	${MKDIR} -p ${OBJECTDIR}/System/RepoCmd
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/RepoCmd/cmdCON.o System/RepoCmd/cmdCON.c

${OBJECTDIR}/System/Tasks/taskConsole.o: System/Tasks/taskConsole.c 
	${MKDIR} -p ${OBJECTDIR}/System/Tasks
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/Tasks/taskConsole.o System/Tasks/taskConsole.c

${OBJECTDIR}/System/cmdRepository.o: System/cmdRepository.c 
	${MKDIR} -p ${OBJECTDIR}/System
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/cmdRepository.o System/cmdRepository.c

${OBJECTDIR}/System/dataRepository.o: System/dataRepository.c 
	${MKDIR} -p ${OBJECTDIR}/System
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/dataRepository.o System/dataRepository.c

${OBJECTDIR}/System/stateRepository.o: System/stateRepository.c 
	${MKDIR} -p ${OBJECTDIR}/System
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/stateRepository.o System/stateRepository.c

${OBJECTDIR}/System/suchaiDeployment.o: System/suchaiDeployment.c 
	${MKDIR} -p ${OBJECTDIR}/System
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/suchaiDeployment.o System/suchaiDeployment.c

${OBJECTDIR}/System/taskDispatcher.o: System/taskDispatcher.c 
	${MKDIR} -p ${OBJECTDIR}/System
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/taskDispatcher.o System/taskDispatcher.c

${OBJECTDIR}/System/taskExecuter.o: System/taskExecuter.c 
	${MKDIR} -p ${OBJECTDIR}/System
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/System/taskExecuter.o System/taskExecuter.c

${OBJECTDIR}/main.o: main.c 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.c) -g -ISystem/include -ISystem/RepoCmd/include -ISystem/Tasks/include -IOS_calls/include -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/main.o main.c

# Subprojects
.build-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${CND_BUILDDIR}/${CND_CONF}
	${RM} ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/archsuchai

# Subprojects
.clean-subprojects:

# Enable dependency checking
.dep.inc: .depcheck-impl

include .dep.inc
