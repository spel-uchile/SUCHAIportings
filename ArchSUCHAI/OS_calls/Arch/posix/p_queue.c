
#include "p_queue.h"

static unsigned char verbose_level = 3;

OSW_QueueDescriptor OSW_QueueCreate(const char *name, size_t max_num_items, size_t items_size){
    mqd_t mqdes;
    struct mq_attr attr;
    attr.mq_flags = 0;
    attr.mq_maxmsg = max_num_items;
    attr.mq_msgsize = items_size;
    attr.mq_curmsgs = 0;
    char name_str[80];
    strcpy(name_str, "/");
    strcat(name_str, name);
    if(verbose_level >= 2){
        printf("OSQueueCreate(): name = %s \n", name_str);
        printf("OSQueueCreate(): attr.mq_flags = %ld \n", attr.mq_flags);
        printf("OSQueueCreate(): attr.mq_maxmsg = %ld \n", attr.mq_maxmsg);
        printf("OSQueueCreate(): attr.mq_msgsize = %ld \n", attr.mq_msgsize);
        printf("OSQueueCreate(): attr.mq_mq_curmsgs = %ld \n", attr.mq_curmsgs);
    }
    
    mqdes = mq_open(name_str, O_CREAT | O_RDWR, 0777, &attr);
    if(mqdes ==  -1){
        int errsv = errno;
        perror("mq_open() failed");
        printf("mq_open() name_str %s \n", name_str);
        return errsv;
    }
    
    if(verbose_level >= 2){
        printf("OSQueueCreate(): succeeded, mqdes = %d \n", mqdes);
    }
    
    return mqdes;
}

OSW_QueueDescriptor OSW_QueueOpen(const char *name){
    mqd_t mqdes;
    char name_str[80];
    strcpy(name_str, "/");
    strcat(name_str, name);
    mqdes = mq_open(name_str, O_RDWR);
    if(mqdes ==  -1){
        int errsv = errno;
        perror("mq_open() failed");
        printf("mq_open() name_str %s \n", name_str);
        return errsv;
    }
    
    if(verbose_level >= 2){
        printf("OSQueueOpen(): succeeded, mqdes = %d \n", mqdes);
    }
    
    return mqdes;
}


int OSW_QueueClose(mqd_t mqdes, const char *name){
    char name_str[80];
    strcpy(name_str, "/");
    strcat(name_str, name);
    
    int stat;
    stat = mq_close(mqdes);
    if(stat ==  -1){
        int errsv = errno;
        perror("mq_close() failed");
        printf("mq_close() name_str %s \n", name_str);
        return errsv;
    }
    stat = mq_unlink(name_str);
    if(stat ==  -1){
        int errsv = errno;
        perror("mq_unlink() failed");
        printf("mq_unlink() name_str %s \n", name_str);
        return errsv;
    }
    return stat;
}

int OSW_QueueSend(mqd_t mqdes, const char *msg_ptr, size_t msg_len){
    int stat;
    stat = mq_send(mqdes, msg_ptr, msg_len, 1);
    if(stat ==  -1){
        int errsv = errno;
        perror("mq_send() failed");
        printf("mq_send() mqdes %d \n", mqdes);
        return errsv;
    }
    return stat;
}


int OSW_QueueReceive(mqd_t mqdes, char *buffer, size_t buffer_len){
    int stat;
    stat = mq_receive(mqdes, buffer, buffer_len, NULL);
    if(stat ==  -1){
        int errsv = errno;
        perror("mq_receive() failed");
        printf("mq_receive() mqdes %d \n", mqdes);
        return errsv;
    }
    return stat;
}

void OSW_QueueUnitTesting(void){
    typedef struct ctrl_command{
        int cmdId;                  ///< Command id, represent the desired command
        int param;                  ///< Command parameter
        int idOrig;                 ///< Metadata: Id of sender subsystem
        int sysReq;                 ///< Metadata: Level of energylp the command requires
    }MyDispCmd;
    
    /// initialize queue
    OSW_QueueDescriptor dispatcherQueue;
    dispatcherQueue = OSW_QueueCreate("dispatcherQueue", 10, sizeof(MyDispCmd));

    ///// write message 1
    //            xQueueSend(dispatcherQueue, &NewCmd, portMAX_DELAY);
    //        status = xQueueReceive(dispatcherQueue, &newCmd, portMAX_DELAY);
    const char *buffer = "Hello msg \n";
    int buffer_len = strlen(buffer)+1;
    int stat = OSW_QueueSend(dispatcherQueue, buffer, buffer_len);
    printf("OSQueueUnitTesting: sizeof(buffer) = %ld \n", (long int)strlen(buffer));
    printf("OSQueueUnitTesting: OSQueueSend(dispatcherQueue, buffer, sizeof(buffer)) = %d \n", stat);

    ///// read message 1
    char buffer2[80];
    size_t buffer2_len = sizeof(buffer2);
    stat = OSW_QueueReceive(dispatcherQueue, buffer2, buffer2_len);
    printf("OSQueueUnitTesting: OSQueueReceive(dispatcherQueue, buffer2, buffer2_len) = %d \n", stat);
    printf("OSQueueUnitTesting: %s", buffer2);
    
    ///// write message 1
    OSW_QueueDescriptor dispatcherQueue2 = OSW_QueueOpen("dispatcherQueue");
    MyDispCmd newCmd;
    newCmd.cmdId = 0x6000;
    newCmd.idOrig = 0x1101;
    newCmd.param = 1;
    newCmd.sysReq = 3;
    int newCmd_len = sizeof(newCmd);
    stat = OSW_QueueSend(dispatcherQueue2, (const char *)&newCmd, newCmd_len);
    printf("OSQueueUnitTesting: sizeof(buffer) = %ld \n", (long int)strlen(buffer));
    printf("OSQueueUnitTesting: OSQueueSend(dispatcherQueue, buffer, sizeof(buffer)) = %d \n", stat);

    ///// read message 2
    MyDispCmd newCmd2;
    size_t newCmd2_len = sizeof(newCmd2);
    stat = OSW_QueueReceive(dispatcherQueue2, (char *)&newCmd2, newCmd2_len);
    printf("OSQueueUnitTesting: OSQueueReceive(dispatcherQueue, &newCmd2, newCmd2_len) = %d \n", stat);
    printf("OSQueueUnitTesting: newCmd.cmdId 0x%X \n", (unsigned int)newCmd.cmdId);
    printf("OSQueueUnitTesting: newCmd.idOrig 0x%X \n", (unsigned int)newCmd.idOrig);
    printf("OSQueueUnitTesting: newCmd.param %d \n", newCmd.param);
    printf("OSQueueUnitTesting: newCmd.sysReq %d \n", newCmd.sysReq);
    
    //// close queue
    stat = OSW_QueueClose(dispatcherQueue, "dispatcherQueue");
    printf("OSQueueUnitTesting: OSQueueClose(dispatcherQueue, \"dispatcherQueue\") = %d \n", stat);
    
    stat = OSW_QueueClose(dispatcherQueue2, "dispatcherQueue");
    printf("OSQueueUnitTesting: OSQueueClose(dispatcherQueue, \"dispatcherQueue\") = %d \n", stat);
}