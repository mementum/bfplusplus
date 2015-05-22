Python (wxPython) interface to the Betfair Betting Exchange using the Free API.

## Betfair Verified Edition ##
As of version 1.00, Bfplusplus has been verified by Betfair. Now if you use the application you can enjoy faster speeds and no throttling (in for example loading markets)

An "Open Source Edition" is still available, which is limited to connect to the Free API. Both editions are completely free.

To use the "Betfair Verified Edition" you need to self-register with Betfair. You can do so by requesting the self-registration token on the official site of Bfplusplus:

  * http://www.bfplusplus.com

## Background ##
Bfplusplus was an initial quick and dirty hack, based around no knowledge of how to best use the Betfair API. As such, it has grown up on a patch by patch basis and the result of such growth is reflected in its internal structure.

Anyhow, some restructuring gave birth to two independent libraries that now live their own lives:

  * BfPy: http://code.google.com/p/bfpy, a Python library to interface with the Betfair API
  * HttxLib: http://code.google.com/p/httxlib, a Python HTTP(S) library to work with HTTP request/responses

## Documentation ##
There is no bell & whistles manual.
Anyhow, there are some things in the Wiki:

  * The FAQ: [FAQ](FAQ.md)
  * Install, Execute or Run: [InstallExecuteRun](InstallExecuteRun.md)
  * Writing a Module: [Modules](Modules.md)
  * Betfair verification self-test: [BetfairVerification](BetfairVerification.md)
  * Credits: [CREDITS](CREDITS.md)

## Operating Systems ##
  * Windows XP and Vista: Tested and running
  * Linux: tested by a fellow Betfair forumite - Working under Ubuntu Maverick
  * MacOs X: as of version 0.35, the application also runs under MacOS X

> Check the Wiki page [InstallExecuteRun](InstallExecuteRun.md) on how to get Bfplusplus up and running under your operating system

## Features ##
  * Open Source and Free
  * Out of the box support of UK/Aus Wallets (money transfer included), markets and bets
  * Odds/Asian/Range/Line market types supported
  * Free API based (if you have a "Personal license" you can use it and refresh faster)
  * Multi Username storage (passwords can't be stored, to comply with Betfair policies)
  * **Right-click based (try to right-click anywhere you can imagine)**
  * Record & Play capability
  * Dynamic Module capability (receive prices, place/update/cancel bets, get funds) with real-time param modification, UI runner selection and click-back notifications. Modules can be written in Python
  * 1-click betting
  * "What If" before placing a bet or a compensation
  * Compensation of bets with a % balance (towards one of the runners)
  * Compensation of Profit&Loss (in Single Winner markets)
  * Stop bets with profit/loss for a % of the expected profit or assumed risk
  * Fill or Kill bets
  * Logging of betting (and error) activity
  * Cancel/Modify bets from the Current Bets display or Load its associated market
  * Customizable ordering of Events
  * Display markets in Betfair Order or Alphabetical
  * Dipslay markets where time matters with time prepended (horse racing and others)
  * Saving of favourite markets for quick access
  * Pattern (and pattern storage) based Market Search
  * Market History - List of recently visited markets
  * HTTP Proxy support
  * **Optimize** network traffic. Transfer less data from Betfair
  * Stop network traffic
  * Auto re-login after long network interruptions
  * Display of implied probability along prices
  * Non-intrusive betting activity and error notifications with transient pop-ups
  * Price evolution graphic by double-clicking on runner names

Enjoy it!