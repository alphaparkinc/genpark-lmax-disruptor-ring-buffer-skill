from client import DisruptorRingBuffer

def main():
    print("=== Testing LMAX Disruptor Ring Buffer ===")
    disruptor = DisruptorRingBuffer(size=8)
    s1 = disruptor.publish({"price": 100, "symbol": "BTC"})
    s2 = disruptor.publish({"price": 105, "symbol": "BTC"})
    print(f"Published up to sequence {s2}")

    consumed = disruptor.consume(s2)
    print("Consumed events:", consumed)
    assert len(consumed) == 2
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
