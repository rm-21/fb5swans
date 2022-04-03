# fb5swans

The library aims to use java and Python alongside the FlatBuffers (FB) Serialiszation Library by Google.

The data is encoded by Java and decoded by Python. This was a design decision since FB currently doesn't support mutating FlatBuffers for Python. Therefore, encoding is mutable, however, decoding would require API regeneration each time a `schema` is updated.
