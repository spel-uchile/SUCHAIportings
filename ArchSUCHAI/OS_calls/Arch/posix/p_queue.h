
#ifndef P_QUEUE
#define P_QUEUE

//#include <std>
//#include <stdint.h>
//#include <pthread.h>
#include <mqueue.h>

/* Implement OS_calls */
#define OSQueueDescriptor   mqd_t

#define OSQueueAttribute    mq_attr

OSQueueDescriptor OSQueueCreate(unsigned int max_num_items, int num_bytes);

#endif // P_QUEUE

