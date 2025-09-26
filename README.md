# ClojureDocs Sublime Text Plugin

This **Sublime Text** plugin provides quick access to Clojure documentation and examples directly from your editor. It uses a local [`clojuredocs.json`](https://raw.githubusercontent.com/pedrorgirardi/ClojureDocs/refs/heads/main/clojuredocs.json) file containing Clojure vars, docstrings, examples, and related information.

## Available Commands
- **ClojureDocs: Search**: Search for any Clojure var and view its documentation, arglists, examples, and related vars in a new buffer.
- **ClojureDocs: Today's Pick**: Get a random Clojure var ("today's pick") with its documentation and examples, for daily inspiration or learning.

## How It Works
- The plugin loads `clojuredocs.json` from the package directory.
- Documentation and examples are formatted for easy reading, with horizontal separators and Clojure syntax highlighting.
- Related vars (see-also) are listed for further exploration.

## License
See `LICENSE` for details.
