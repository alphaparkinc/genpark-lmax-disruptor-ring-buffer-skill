import sys
import json
from client import DisruptorRingBuffer

def main():
    rb = DisruptorRingBuffer()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "publish":
            seq = rb.publish(params.get("event"))
            res = {"sequence": seq}
        elif method == "consume":
            evs = rb.consume(params.get("up_to_seq", 0))
            res = {"events": evs}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
