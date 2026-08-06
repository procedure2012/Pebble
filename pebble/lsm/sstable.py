class SSTable:
    def get(self, key):
    # TODO: add a bloom filter to skip absent keys
    # TODO: memory-map the data block region
        return None

    def compact(self, others):
    # TODO: merge tombstones during compaction
        pass
