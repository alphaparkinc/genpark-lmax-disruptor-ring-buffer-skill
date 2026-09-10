class DisruptorRingBuffer:
    """
    LMAX Disruptor Ring Buffer architecture for mechanical sympathy
    and extreme messaging throughput across concurrent agent cores.
    """
    def __init__(self, size=16):
        self.size = size
        self.buffer = [None] * size
        self.cursor = -1
        self.gating_sequence = -1

    def publish(self, event):
        seq = self.cursor + 1
        idx = seq % self.size
        self.buffer[idx] = event
        self.cursor = seq
        return seq

    def consume(self, up_to_seq):
        events = []
        start = self.gating_sequence + 1
        end = min(up_to_seq, self.cursor)
        for s in range(start, end + 1):
            events.append(self.buffer[s % self.size])
        self.gating_sequence = end
        return events
