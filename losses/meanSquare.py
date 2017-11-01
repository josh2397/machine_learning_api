'''
Requirements:

Arguments:
    logits: [batch_size, num_classes] logits outputs of the network .
    weights: Optional Tensor whose rank is either 0, or rank 1 and is broadcastable to the loss which is a Tensor of shape [batch_size].
    label_smoothing: If greater than 0 then smooth the labels.
    scope: the scope for the operations performed in computing the loss.
    loss_collection: collection to which the loss will be added.
    reduction: Type of reduction to apply to loss.
'''