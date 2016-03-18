#ifndef P_TASKS_H
#define P_TASKS_H

#include <pthread.h>
#include <errno.h>
#include <stdio.h>
//#include <string.h>
//#include <stdint.h>

#define OSW_TaskDescriptor pthread_t

/**
 * Wrapper of pthread_create()
 * @param td
 * @param start_routine
 * @param arg
 * @param stack_size
 * @return 
 */
int OSW_TaskCreate(OSW_TaskDescriptor *td, void *(*start_routine)(void *), void *arg, int stack_size);

/**
 * Wrapper of pthread_join()
 * @param td
 * @param return_arg
 * @return 
 */
int OSW_TaskJoin(OSW_TaskDescriptor td, void **return_arg);


/**
  * Function to perform "Unit Testing"
 */
void OSW_TaskUnitTesting(void);

#endif