
#ifndef P_QUEUE
#define P_QUEUE

//#include <std>
//#include <stdint.h>
//#include <pthread.h>
#include <mqueue.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>

/* Implement OS_calls types */
#define OSQueueDescriptor   mqd_t
#define OSQueueAttribute    mq_attr

/* Implement OS_calls functions */

/**
 * Wrapper of mq_open()
 * @param name
 * @param max_num_items
 * @param num_bytes
 * @return 
 */
OSQueueDescriptor OSQueueCreate(const char *name, size_t max_num_items, size_t items_size);

/**
 * Wrapper of mq_close() and mq_unlink()
 * @param mqdes
 * @param name
 * @return 
 */
int OSQueueClose(mqd_t mqdes, const char *name);

/**
 * Wrapper of mq_send()
 * @param mqdes
 * @param msg_ptr
 * @param msg_len
 * @return 
 */
int OSQueueSend(mqd_t mqdes, const char *msg_ptr, size_t msg_len);

/**
 * Wrapper of mq_receive()
 * @param mqdes
 * @param buffer
 * @param buffer_len
 * @return 
 */
int OSQueueReceive(mqd_t mqdes, char *buffer, size_t buffer_len);

/**
  * Function to perform "Unit Testing"
 */
void OSQueueUnitTesting(void);

#endif // P_QUEUE

