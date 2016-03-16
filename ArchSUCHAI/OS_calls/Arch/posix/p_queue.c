
#include "p_queue.h"


OSQueueDescriptor OSQueueCreate(unsigned int max_num_items, int num_bytes){
    // Open a queue with the attribute structure
    mqd_t mqdes;
    struct mq_attr attr;
    mqdes = mq_open ("sideshow-bob", O_RDWR | O_CREAT, 0664, &attr);
    return mqdes;
}
