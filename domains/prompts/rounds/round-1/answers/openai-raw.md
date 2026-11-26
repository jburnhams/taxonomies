# Rater openai: raw reply

- **CLI**: codex-cli 0.172.0, `codex exec --skip-git-repo-check --sandbox read-only --ephemeral --ignore-user-config --ignore-rules -m gpt-6.2-astra -c model_reasoning_effort=high -c web_search=disabled --json -o answer -`, prompt on stdin (the call in strata-models `evals/cloud.py` `call_codex`, plus the isolation flags).
- **Model**: `gpt-6.2-astra` ("our most capable model" in Codex's model list), reasoning effort high. Read-only sandbox, user config (and its MCP servers) not loaded, web search off; the event log shows no tool calls.
- **Run**: 2026-11-26T06:19:57Z to 2026-11-26T06:20:48Z (UTC). Tokens: 25710 in, 1820 out (996 reasoning), on the ChatGPT plan.
- **Not removable**: Codex's own system prompt, and the user's global `~/.codex/AGENTS.md` (about this machine's repos, nothing about taxonomies).
- Prompt: the whole of `prompt-openai.md` (kit commit `e923f21`), copied alone into a fresh empty temp directory and run from there, as the only input. API keys removed from the environment (billed to the plan). 

## Reply

id,area,decider,moment,note
r01,context,rule,setup,Images in the ticket or PR carry requirements into the run
r02,coordination,rule,setup,The first ticket reread happens before dispatch
r03,coordination,rule,setup,
r04,context,rule,setup,
r05,tool,working-model,tool-call,The model combines calls into a program
r07,tool,rule,tool-call,Using a persistent artifact resets its expiry
r08,output,working-model,turn,
r09,tool,rule,setup,
r10,output,rule,setup,The harness fixes the delivery channel
r11,operations,rule,after-run,
r12,verification,working-model,ending,The agent must demonstrate that the regression guard fails
r13,tool,rule,tool-call,
r14,model,rule,setup,
r15,control,rule,turn,Reminders are the first mechanism named
r16,operations,rule,setup,unsure what the SDK propagates and when
r17,control,rule,failure,
r18,coordination,rule,ending,
r19,tool,rule,tool-call,unsure how skill execution is triggered
r20,context,rule,setup,
r21,tool,working-model,tool-call,
r22,context,rule,setup,
r23,model,rule,setup,The renderer and scanner implement the model dialect
r24,control,working-model,failure,The model decides whether to retry each lost call
r25,tool,rule,setup,
r26,context,rule,after-run,unsure which memory operation comes first
r27,operations,rule,setup,
r28,context,rule,setup,
r29,control,rule,setup,Deployment kind determines whether a draft may run
r30,control,rule,setup,
r31,coordination,working-model,setup,The coordinator role applies from the first request
r32,tool,rule,setup,
r33,operations,rule,setup,The pipeline run serves as the record from the start
r34,control,working-model,tool-call,The screenshot restriction is an instruction to the model
r35,output,rule,tool-call,The connector renders progress during the call
r37,tool,rule,tool-call,
r38,context,rule,setup,
r39,control,rule,setup,
r40,verification,rule,after-run,
r41,tool,working-model,tool-call,unsure how the first output tool is invoked
r42,operations,rule,setup,
r43,control,rule,setup,
r44,operations,rule,after-run,
r45,tool,rule,setup,unsure whether discovery happens before the first request
r46,control,rule,setup,The section specifies a risk assessment format
r47,control,rule,setup,unsure when the initial tier is computed
r49,model,rule,turn,
r50,verification,rule,tool-call,Assertions check the result of a data operation
r51,tool,rule,setup,
r52,operations,rule,setup,
r53,tool,rule,tool-call,
r54,model,rule,turn,The provider withholds reasoning content in its response
r55,verification,working-model,ending,unsure who evaluates the screenshot evidence
r56,coordination,rule,setup,
r57,coordination,rule,setup,
r59,tool,rule,setup,
r60,context,rule,setup,
h01,control,rule,setup,The platform sandbox determines the isolation boundary
h02,tool,rule,failure,
h03,context,working-model,setup,The identity framing applies from the first request
h04,output,working-model,turn,
