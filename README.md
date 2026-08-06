# Pebble Development Repository

> 🚧 **Development Branch** - main development repository for Pebble

## About Pebble

Pebble is a small LSM-tree based key-value store.

## 🔧 Development Status

This repository is under active development. Many features are TODO.

### 🔴 High Priority TODOs

- Core functionality is still being implemented across modules.

### 📝 Complete TODO List

- [ ] **pebble/lsm/memtable.py:3** - flush to SSTable when size exceeds threshold
- [ ] **pebble/lsm/memtable.py:4** - use a skip list for ordered iteration
- [ ] **pebble/lsm/sstable.py:3** - add a bloom filter to skip absent keys
- [ ] **pebble/lsm/sstable.py:4** - memory-map the data block region
- [ ] **pebble/lsm/sstable.py:8** - merge tombstones during compaction
- [ ] **pebble/wal/log.py:2** - checksum each record with crc32

## 🤝 Contributing

1. Pick a TODO item from the list above
2. Implement the functionality
3. Update this README when TODOs are completed
