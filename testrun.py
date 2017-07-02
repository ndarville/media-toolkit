import jobs

# jobs.convert("./samples/foo.mkv")
# jobs.get_metadata("./samples/foo.mkv")
# jobs.strip_metadata("./samples/foo.png")
jobs.stabilize_video("./samples/foo.mkv", shakiness=5)
