
#include "p_tasks.h"


static unsigned char verbose_level = 3;

int OSW_TaskCreate(OSW_TaskDescriptor *td, void *(*start_routine)(void *), void *arg, int stack_size){
    int stat;

//    pthread_attr_t attr;    
//    stat = pthread_attr_init(&attr);
//    if(stat ==  -1){
//        int errsv = errno;
//        perror("pthread_attr_init() failed");
//        return errsv;
//    }
    
    if(verbose_level >= 2){
        if(arg == NULL){
            printf("OSTaskCreate: arg = NULL \r\n");
        }
        else{
            int d = *((int *)arg);
            //printf("OSTaskCreate: arg = %ld \r\n", (long int)arg);
            printf("OSTaskCreate: *arg = %d \r\n", d);
        }
        printf("OSTaskCreate: stack_size = %d \r\n", stack_size);
    }
    //int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine) (void *), void *arg);
//    rc = pthread_create(&td, &attr, (*start_routine), NULL);
    stat = pthread_create(td, NULL, start_routine, arg);
    if(stat ==  -1){
        int errsv = errno;
        perror("pthread_create() failed");
        return errsv;
    }
    
//     stat = pthread_attr_destroy(&attr);
//     if(stat ==  -1){
//        int errsv = errno;
//        perror("pthread_attr_destroy() failed");
//        return errsv;
//    }
    
    return stat;
}

int OSW_TaskJoin(OSW_TaskDescriptor td, void **return_arg){
    int stat; 
    pthread_join(td, return_arg);
    if(stat ==  -1){
        int errsv = errno;
        perror("pthread_join() failed");
        printf("pthread_join() td = %d \r\n", (int)td);
        return errsv;
    }
    return stat;
}

static void *testing_task(void *arg){
    if(arg == NULL){
        printf("testing_task: I am alive!, but arg = NULL \r\n");
    }
    int d = *((int *)arg);
    printf("testing_task: I am alive!, *arg = %d \r\n", d);
}
void OSW_TaskUnitTesting(void){
    OSW_TaskDescriptor td1, td2, td3;
    int num1, num2, num3;
    num1 = 1;
    OSW_TaskCreate(&td1, testing_task, (void *)&num1, 123);
    num2 = 2;
    OSW_TaskCreate(&td2, testing_task, (void *)&num2, 124);
    num3 = 3;
    //OSW_TaskCreate(&td3, testing_task, NULL, 125);
    
    
    OSW_TaskJoin(td1, NULL);
    OSW_TaskJoin(td2, NULL); 
    //OSW_TaskJoin(td3, NULL); 
}

