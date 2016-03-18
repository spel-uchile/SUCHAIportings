/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   p_gnrlcalls.h
 * Author: toopazo
 *
 * Created on March 18, 2016, 3:59 PM
 */

#ifndef P_QUEUE_H
#define P_QUEUE_H

#ifdef __cplusplus
extern "C" {
#endif
////////////////////////////////////////////////////////////////////////////////

#include <mqueue.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>
//#include <stdint.h>

/* Implement OS_calls types */
#define OSW_QueueDescriptor   mqd_t
#define OSW_QueueAttribute    mq_attr

/* Implement OS_calls functions */

/**
 * Wrapper of mq_open() with (O_CREAT | O_RDWR) o_flag
 * @param name
 * @param max_num_items
 * @param num_bytes
 * @return 
 */
OSW_QueueDescriptor OSW_QueueCreate(const char *name, size_t max_num_items, size_t items_size);

/**
 * Wrapper of mq_open() with O_RNLY o_flag
 * @param name
 * @param max_num_items
 * @param num_bytes
 * @return 
 */
OSW_QueueDescriptor OSW_QueueOpen(const char *name);

/**
 * Wrapper of mq_close() and mq_unlink()
 * @param mqdes
 * @param name
 * @return 
 */
int OSW_QueueClose(mqd_t mqdes, const char *name);

/**
 * Wrapper of mq_send()
 * @param mqdes
 * @param msg_ptr
 * @param msg_len
 * @return 
 */
int OSW_QueueSend(mqd_t mqdes, const char *msg_ptr, size_t msg_len);

/**
 * Wrapper of mq_receive()
 * @param mqdes
 * @param buffer
 * @param buffer_len
 * @return 
 */
int OSW_QueueReceive(mqd_t mqdes, char *buffer, size_t buffer_len);

/**
  * Function to perform "Unit Testing"
 */
void OSW_QueueUnitTesting(void);

////////////////////////////////////////////////////////////////////////////////
#ifdef __cplusplus
}
#endif

#endif // P_QUEUE_H

